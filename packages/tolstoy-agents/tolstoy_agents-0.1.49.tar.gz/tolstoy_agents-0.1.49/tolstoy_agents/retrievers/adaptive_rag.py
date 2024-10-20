import functools
from typing import List
from typing_extensions import TypedDict
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain_core.output_parsers import StrOutputParser

#from langchain.schema import Document
from langgraph.graph import END, StateGraph

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

MAX_RETRIEVES = 2

rag_prompt = hub.pull_prompt("rlm/rag-prompt")

system = """You are a grader assessing relevance of a retrieved document to a user question. \n 
If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""
grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Retrieved document: \n\n {document} \n\n User question: {question}"),
    ]
)

system = """You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts. \n 
Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""
hallucination_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Set of facts: \n\n {documents} \n\n LLM generation: {generation}"),
    ]
)

system = """You are a grader assessing whether an LLM generation answers question. \n 
Give a binary score 'yes' or 'no'. 
'yes' means that the LLM generation has an direct answer to the question belows.
"""
answer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "User question: \n\n {question} \n\n LLM generation: {generation}"),
    ]
)

system = """You a question re-writer that converts an input question to a better version that is optimized \n 
for vectorstore retrieval. Look at the input and try to reason about the underlying sematic intent / meaning."""
re_write_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        (
            "human",
            "Here is the initial question: \n\n {question} \n Formulate an improved question.",
        ),
    ]
)

# Data model

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        n_retrieves: number of requests to retriever
        question: question
        generation: LLM generation
        documents: list of documents
    """
    n_retrieves: int
    question: str
    generation: str
    documents: List[str]


class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""

    binary_score: str = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )


class GradeAnswer(BaseModel):
    """Binary score to assess answer addresses question."""

    binary_score: str = Field(
        description="Answer addresses the question, 'yes' or 'no'"
    )


class GradeHallucinations(BaseModel):
    """Binary score for hallucination present in generation answer."""

    binary_score: str = Field(
        description="Answer is grounded in the facts, 'yes' or 'no'"
    )


def retrieve(state, vectorstore):
    """
    Retrieve documents

    Args:
        state (dict): The current graph state
        vectorstore: Pinecone vectorstore

    Returns:
        state (dict): New key added to state, documents, that contains retrieved documents
    """
    retriever = vectorstore.as_retriever()

    print("---RETRIEVE---")
    question = state["question"]
    n_retrieves = state.get('n_retrieves') if state.get('n_retrieves') else 0

    # Retrieval
    documents = retriever.invoke(question, k=2)
    return {"documents": documents, "n_retrieves": n_retrieves + 1}


def generate(state, rag_chain):
    """
    Generate answer

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, generation, that contains LLM generation
    """
    print("---GENERATE---")
    question = state["question"]
    documents = state["documents"]
    n_retrieves = state["n_retrieves"]

    if n_retrieves>MAX_RETRIEVES:
        return {"generation": f"No answer found over {MAX_RETRIEVES} tries."}
    # RAG generation
    generation = rag_chain.invoke({"context": documents, "question": question})
    return {"generation": generation}


def grade_documents(state, retrieval_grader):
    """
    Determines whether the retrieved documents are relevant to the question.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates documents key with only filtered relevant documents
    """

    print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
    question = state["question"]
    documents = state["documents"]

    # Score each doc
    filtered_docs = []
    for d in documents:
        score = retrieval_grader.invoke(
            {"question": question, "document": d.page_content}
        )
        grade = score.binary_score
        if grade == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            filtered_docs.append(d)
        else:
            print("---GRADE: DOCUMENT NOT RELEVANT---")
            continue
    return {"documents": filtered_docs}


def transform_query(state, question_rewriter):
    """
    Transform the query to produce a better question.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates question key with a re-phrased question
    """

    print("---TRANSFORM QUERY---")
    question = state["question"]
    documents = state["documents"]

    # Re-write question
    better_question = question_rewriter.invoke({"question": question})
    return {"question": better_question}


### Edges ###

def decide_to_generate(state):
    """
    Determines whether to generate an answer, or re-generate a question.

    Args:
        state (dict): The current graph state

    Returns:
        str: Binary decision for next node to call
    """

    print("---ASSESS GRADED DOCUMENTS---")
    question = state["question"]
    filtered_documents = state["documents"]

    if not filtered_documents:
        # All documents have been filtered check_relevance
        # We will re-generate a new query
        print(
            "---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---"
        )
        return "transform_query"
    else:
        # We have relevant documents, so generate answer
        print("---DECISION: GENERATE---")
        return "generate"


def grade_generation_v_documents_and_question(state, hallucination_grader, answer_grader):
    """
    Determines whether the generation is grounded in the document and answers question.

    Args:
        state (dict): The current graph state

    Returns:
        str: Decision for next node to call
    """

    print("---CHECK HALLUCINATIONS---")
    question = state["question"]
    documents = state["documents"]
    generation = state["generation"]
    n_retrieves = state["n_retrieves"]

    score = hallucination_grader.invoke(
        {"documents": documents, "generation": generation}
    )
    grade = score.binary_score

    # Check hallucination
    if grade == "yes":
        print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
        # Check question-answering
        print("---GRADE GENERATION vs QUESTION---")
        score = answer_grader.invoke({"question": question, "generation": generation})
        grade = score.binary_score
        if grade == "yes":
            print("---DECISION: GENERATION ADDRESSES QUESTION---")
            return "useful"
        elif n_retrieves>MAX_RETRIEVES:
            print(f"---DECISION: REACHED LIMIT NUMBER OF RETRIEVS: {MAX_RETRIEVES} ---")
            return "max_retrieves"
        else:
            print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
            return "not useful"
    else:
        if n_retrieves>MAX_RETRIEVES:
            print(f"---DECISION: REACHED LIMIT NUMBER OF RETRIEVS: {MAX_RETRIEVES} ---")
            return "max_retrieves"

        print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
        return "not useful"#"not supported"


def adaptive_rag(llm_model, retrieve_node):
    retrieval_grader = grade_prompt | llm_model.with_structured_output(GradeDocuments)
    rag_chain = rag_prompt | llm_model | StrOutputParser()
    hallucination_grader = hallucination_prompt | llm_model.with_structured_output(GradeHallucinations)
    answer_grader = answer_prompt | llm_model.with_structured_output(GradeAnswer)
    question_rewriter = re_write_prompt | llm_model | StrOutputParser()

    workflow = StateGraph(GraphState)

    # Define the nodes
    workflow.add_node("retrieve",        retrieve_node)
    workflow.add_node("grade_documents", functools.partial(grade_documents,
                                                           retrieval_grader = retrieval_grader))
    workflow.add_node("generate",        functools.partial(generate,
                                                           rag_chain = rag_chain))
    workflow.add_node("transform_query", functools.partial(transform_query,
                                                           question_rewriter = question_rewriter))

    # Build graph
    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "grade_documents")
    workflow.add_conditional_edges(
        "grade_documents",
        decide_to_generate,
        {
            "transform_query": "transform_query",
            "generate": "generate",
        },
    )
    workflow.add_edge("transform_query", "retrieve")
    workflow.add_conditional_edges(
        "generate",
        functools.partial(grade_generation_v_documents_and_question,
                          hallucination_grader = hallucination_grader,
                          answer_grader = answer_grader),
        {
            "not supported": "generate",
            "useful": END,
            "not useful": "transform_query",
            "max_retrieves": END
        },
    )

    workflow_compiled = workflow.compile()

    return workflow_compiled


if __name__ == "__main__":
    # LLM with function call
    llm = ChatOpenAI(model="gpt-4-1106-preview", 
                     temperature=0,
                     verbose=True)

    print(llm)
    
    # Set embeddings
    embd = OpenAIEmbeddings()

    # Docs to index
    urls = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
    ]

    # Load
    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]

    # Split
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=500, chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(docs_list)

    # Add to vectorstore
    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=embd,
    )
    retrieve_node = functools.partial(retrieve, vectorstore = vectorstore)

    #inputs = {"question": "What are the types of agent memory?"}
    inputs = {"question": "What time is it now?"}
    app = adaptive_rag(llm, retrieve_node)
    result = app.invoke(inputs)
    print(result['generation'])
