import os
import functools
from pydantic.v1 import BaseModel, Field
from langchain.tools import StructuredTool
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from tolstoy_agents.utils import (
    docs_to_text,
    handle_exceptions
    )
from tolstoy_agents.retrievers.utils import _query_vectorstore


embedder = OpenAIEmbeddings(
        model = "text-embedding-3-small",
        api_key = os.environ.get('OPENAI_API_KEY'),
    )

class ToolInput(BaseModel):
    text_query: str = Field(..., description=(
        "The query that will be used to search for relevant documents in our knowledge base that is relevant to the customer question or their intent"
        )
    )

@handle_exceptions
def product_documentation(text_query: str,
                          repo_path: str,
                          chunk_size: int,
                           ) -> str:
    relevant_docs = relevant_documents(text_query, repo_path, chunk_size)
    
    res = docs_to_text(relevant_docs)

    return res


def relevant_documents(text_query: str,
                       repo_path: str,
                       chunk_size: int,
                       n_items: int = 2) -> str:
    
    vectorstore = PineconeVectorStore(index_name = "toly-embeddings",
                        embedding = embedder,
                        pinecone_api_key =  os.environ.get('PINECONE_API_KEY'),
                        namespace = "fulltext",
                        text_key = "filepath")
    
    relevant_docs = _query_vectorstore(
                            repo_path,
                            chunk_size,
                            vectorstore,
                            text_query,
                            n_items)

    return relevant_docs


def relevant_documents_factory(
                          repo_path: str,
                          chunk_size: int,
                          n_items: int = 2,
                           ) -> str:
    return functools.partial(
            relevant_documents,
            repo_path=repo_path,
            chunk_size=chunk_size,
            n_items=n_items
        )


def product_documentation_factory(
                            repo_path,
                            chunk_size) -> StructuredTool:
    return StructuredTool.from_function(
        func=functools.partial(
            product_documentation,
            repo_path=repo_path,
            chunk_size=chunk_size,
        ),
        name="product_documentation",
        description= (
            "Contains the product documentation, knowledge base articles, and other relevant information about the Tolstoy product. Use this tool to answer questions about the Tolstoy product, related integrations, etc., even for users without a Tolstoy account."
        ),
        args_schema=ToolInput,
        return_direct=False
    )
