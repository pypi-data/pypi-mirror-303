import argparse

from nxlu.constants import (
    GRAPHRAG_ALGORITHM_DOCUMENT_EXTRACTION_PROMPT,
    GRAPHRAG_ALGORITHM_RELATION_PROMPT,
    GRAPHRAG_ALGORITHM_SYSTEM_PROMPT,
)
from nxlu.explanation.rag import GraphRAGPipeline
from nxlu.io import load_algorithm_encyclopedia
from nxlu.utils.misc import normalize_name, parse_algorithms

SUPPORTED_ALGORITHMS, ALGORITHM_CATEGORIES, STANDARDIZED_ALGORITHM_NAMES = (
    parse_algorithms(load_algorithm_encyclopedia(), normalize_name)
)


def main(
    documents_path: str,
    corpus_path: str,
    allowed_nodes: list,
    relationship_prompt: str,
    extraction_prompt: str,
    system_prompt: str,
    corpus_embedding_model: str,
    rag_model: str,
    neo4j_db: str,
):
    """Run the GraphRAGPipeline with the provided paths and parameters.

    Parameters
    ----------
    documents_path : str
        Path to the JSONL file containing the documents to be processed.
    corpus_path : str
        Path to the text file containing the term corpus.
    allowed_nodes : list
        List of allowed node types.
    relationship_prompt : str
        The prompt template for extracting relationships between nodes.
    extraction_prompt : str
        The prompt template for extracting document details.
    system_prompt : str
        The system prompt to be used by the language model.
    corpus_embedding_model : str
        The model used to generate corpus embeddings.
    rag_model : str
        The retrieval-augmented generation model.
    neo4j_db : str
        The Neo4j database name.
    """
    pipeline = GraphRAGPipeline(
        documents_path=documents_path,
        corpus_path=corpus_path,
        allowed_nodes=allowed_nodes,
        relationship_prompt=relationship_prompt,
        extraction_prompt=extraction_prompt,
        system_prompt=system_prompt,
        corpus_embedding_model=corpus_embedding_model,
        rag_model=rag_model,
        neo4j_db=neo4j_db,
    )
    pipeline.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NxLU -- GraphRAG Pipeline")

    parser.add_argument(
        "--documents_path",
        default="nxlu/data/rag_documents.jsonl",
        help="Path to the JSONL file containing the documents to process. "
        "Default: 'nxlu/data/rag_documents.jsonl'.",
    )

    parser.add_argument(
        "--corpus_path",
        help="Path to the text file containing a term corpus.",
    )

    parser.add_argument(
        "--allowed_nodes",
        default=STANDARDIZED_ALGORITHM_NAMES,
        help="List of allowed node types. Default: STANDARDIZED_ALGORITHM_NAMES.",
    )

    parser.add_argument(
        "--relationship_prompt",
        default=GRAPHRAG_ALGORITHM_RELATION_PROMPT,
        help="Prompt template for extracting relationships. Default: "
        "GRAPHRAG_ALGORITHM_RELATION_PROMPT.",
    )

    parser.add_argument(
        "--extraction_prompt",
        default=GRAPHRAG_ALGORITHM_DOCUMENT_EXTRACTION_PROMPT,
        help="Prompt template for extracting document details. Default: "
        "GRAPHRAG_ALGORITHM_DOCUMENT_EXTRACTION_PROMPT.",
    )

    parser.add_argument(
        "--system_prompt",
        default=GRAPHRAG_ALGORITHM_SYSTEM_PROMPT,
        help="System prompt to be used by the model. Default: "
        "GRAPHRAG_ALGORITHM_SYSTEM_PROMPT.",
    )

    parser.add_argument(
        "--corpus_embedding_model",
        default="witiko/mathberta",
        help="Model used to generate corpus embeddings. Default: witiko/mathberta.",
    )

    parser.add_argument(
        "--rag_model",
        default="gpt-4o-2024-08-06",
        help="Retrieval-augmented generation model. Default: gpt-4o-2024-08-06.",
    )

    parser.add_argument(
        "--neo4j_db",
        default="nxlu",
        help="Neo4j database name. Default: nxlu.",
    )

    args = parser.parse_args()

    main(
        documents_path=args.documents_path,
        corpus_path=args.corpus_path,
        allowed_nodes=args.allowed_nodes,
        relationship_prompt=args.relationship_prompt,
        extraction_prompt=args.extraction_prompt,
        system_prompt=args.system_prompt,
        corpus_embedding_model=args.corpus_embedding_model,
        rag_model=args.rag_model,
        neo4j_db=args.neo4j_db,
    )
