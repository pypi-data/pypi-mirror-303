import argparse
import logging

import networkx as nx
from langchain.schema import Document

from nxlu.constants import ALGORITHM_SUBMODULES, NX_TERM_BLACKLIST
from nxlu.explanation.corpus import (
    assemble_corpus,
    extract_text_by_chunk,
    is_camel_case,
    load_documents_from_directory,
    remove_stop_words,
    save_corpus_as_txt,
    save_docs_to_jsonl,
)
from nxlu.io import load_algorithm_encyclopedia
from nxlu.utils.misc import normalize_name, parse_algorithms

SUPPORTED_ALGORITHMS, ALGORITHM_CATEGORIES, STANDARDIZED_ALGORITHM_NAMES = (
    parse_algorithms(load_algorithm_encyclopedia(), normalize_name)
)

logger = logging.getLogger("nxlu")


def load_networkx_terms(submodules):
    """Load all public terms from the main networkx module and its submodules.

    Parameters
    ----------
    submodules : list
        A list of submodule names (as strings) from which to load additional terms.

    Returns
    -------
    list
        A list of unique public terms (function and class names) from networkx and its
        submodules.
    """
    networkx_terms = set(dir(nx))
    networkx_terms = {term for term in networkx_terms if not term.startswith("_")}

    for submodule in submodules:
        module = nx
        for level in submodule.split(".")[1:]:
            module = getattr(module, level)

        submodule_terms = set(dir(module))
        networkx_terms.update(
            {term for term in submodule_terms if not term.startswith("_")}
        )

    filtered_terms = [
        remove_stop_words(term.replace("_", " "))
        for term in list(set(networkx_terms))
        if term not in NX_TERM_BLACKLIST and not is_camel_case(term)
    ]
    return filtered_terms


def main(pdfs_directory: str):
    logger.info(f"Processing PDFs in directory: {pdfs_directory}")

    documents = load_documents_from_directory(
        pdfs_directory,
        extract_func=lambda path, chunk_size, chunk_overlap: extract_text_by_chunk(
            path,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        ),
    )

    document_objects = [Document(page_content=doc) for doc in documents]

    save_docs_to_jsonl(document_objects)

    networkx_terms = load_networkx_terms(ALGORITHM_SUBMODULES)

    graph_theory_corpus = assemble_corpus(
        documents, networkx_terms, ngram_range=(1, 3), max_features=10000
    )

    logger.info(f"Extracted graph theory terms: {graph_theory_corpus}")

    save_corpus_as_txt(graph_theory_corpus, "graph_theory_corpus.txt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process a directory of PDFs and extract graph theory terms."
    )
    parser.add_argument(
        "pdfs_path",
        type=str,
        help="The path to the directory containing the PDFs to process.",
    )

    args = parser.parse_args()

    main(args.pdfs_path)
