import os
import re
from typing import List

from langchain.schema import Document

from smart_open import open as open_smart

STOCK_FILE_UNAVAILABLE_PROMPT = "There is no file {filepath}"

def _complete_metadata(chunk_size: int, metadata: dict):
    metadata = dict(metadata)
    path = metadata.get('path', None)
    filepath = metadata.get('filepath', None)
    if path is None and filepath is None:
        raise ValueError("metadata must contain either path or filepath")
    elif path is None:
        path = f"{filepath}:0-{chunk_size}"
    elif filepath is None:
        matches = re.findall(r"^(.*?)(?::\d+-\d+)?$", path, re.M)
        if len(matches) == 0:
            raise ValueError(f"Warning - received unexpected vector id: [{path}]")
        filepath = matches[0]

    metadata['path'] = path
    metadata['filepath'] = filepath

    return metadata


def _get_file_content(repo_path: str, filepath: str):
    abs_filepath = os.path.join(repo_path, filepath)
    try:
        with open_smart(abs_filepath, 'r', encoding='utf-8') as f:
            full_content = '\n'.join(line for line in f)
    except OSError:
        print(f"Warning - {filepath} exists in pinecone metadata but not in {repo_path}")
        return STOCK_FILE_UNAVAILABLE_PROMPT.format(filepath=abs_filepath)

    text = full_content
    return text


def _single_text_getter(repo_path: str, chunk_size: int, metadata={}):
    """
    Given the metadata for a LangChain Document, this function returns 
    the text of the document by reading from disk. 
    This is used by the VectorStore to get the text of a document. 
    This function sits here because it relies on the repo_path, 
    which is a config parameter.
    """
    metadata = _complete_metadata(chunk_size, metadata)
    path = metadata.get("path", None)
    filepath = metadata.get("filepath", None)
    if path is None or filepath is None:
        raise ValueError("metadata must contain either path or filepath")

    matches = re.findall(r'(?m).*:(\d+)-(\d+)$', path)
    if len(matches) == 0:
        print(f'Warning - received unexpected vector id: [{path}]')
        return ""

    read_start, read_end = (int(s) for s in matches[0])

    full_content = _get_file_content(repo_path, filepath)
    abs_filepath = os.path.join(repo_path, filepath)
    if full_content == STOCK_FILE_UNAVAILABLE_PROMPT.format(filepath=abs_filepath):
        return STOCK_FILE_UNAVAILABLE_PROMPT.format(filepath=abs_filepath)

    if read_end > len(full_content) + 1:
        print(
            (
                f"Warning - character range [{read_start},{read_end}] is "
                f"invalid for file of length [{len(full_content)+1}], [{path}]"
            )
        )
        # If the read_start point makes sense, use it
        if read_start < len(full_content):
            read_end = len(full_content)
        # Otherwise just take the last chunk
        else:
            read_start = max(0, len(full_content) - chunk_size)

    text = full_content[read_start:read_end]

    return text


def _text_getter(repo_path: str, chunk_size: int, results: list):
    texts = [_single_text_getter(repo_path, chunk_size, res.metadata) for res in results]
    return texts


def _query_vectorstore(
        repo_path: str,
        chunk_size: int,
        vectorstore,
        query: str,
        n_items = 2,
        filter_dict = {}
    ) -> List[Document]:
    """Runs similarity_search on vectorstore.

    Args:
        conf (_type_): _description_
        vectorstore (_type_): _description_
        query (_type_): Text
        n_items (int, optional): _description_. Defaults to 2.
        filter_dict (dict, optional): _description_. Defaults to {}.

    Returns:
        List[Document]: list of closest Documents from vectorstore
    """
    relevant_docs = vectorstore.similarity_search(
        query,
        k = n_items,
        filter = filter_dict
        )

    for doc in relevant_docs:
        doc.metadata = _complete_metadata(chunk_size, doc.metadata)

    relevant_docs_text = _text_getter(repo_path, chunk_size, relevant_docs)

    for ix, doc in enumerate(relevant_docs):
        doc.page_content = relevant_docs_text[ix]

    return relevant_docs


def _get_functions_from_file(repo_path: str, filepath: str):
    _, ext = os.path.splitext(filepath)

    if ext not in ['js']:
        return f'Not implemented for {ext} files.'

    abs_filepath = os.path.join(repo_path, filepath)
    content = _get_file_content(repo_path, filepath)

    if content==STOCK_FILE_UNAVAILABLE_PROMPT.format(filepath=abs_filepath):
        return content

    try:
        arrow_function_patterns = [
            r'const\s+(\w+)\s*=\s*.*?=>',
        ]

        function_names = []

        for pattern in arrow_function_patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                function_names.append(match.group(1))

    except Exception as e:
        print(f"An error occurred: {e}")

    function_names = set(function_names)

    return ','.join(function_names)
