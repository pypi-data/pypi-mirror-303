import importlib.resources as pkg_resources
import json
import logging
import re
import unicodedata
import warnings
from collections import Counter
from collections.abc import Iterable
from pathlib import Path

import numpy as np
from langchain.document_loaders import PyMuPDFLoader
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from nltk import ngrams
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nxlu.constants import NOISE_PATTERNS

warnings.filterwarnings("ignore")

logger = logging.getLogger("nxlu")


def get_package_data_directory() -> Path:
    """Return the path to the `nxlu/data/` directory inside the package."""
    package_data_dir = pkg_resources.files("nxlu") / "data"
    return package_data_dir


def load_documents_from_directory(
    directory_path, extract_func, chunk_size=750, chunk_overlap=500
):
    """Load and extract text from all PDFs in the given directory.

    Parameters
    ----------
    directory_path : str
        The path to the directory containing the PDF files.
    extract_func : function
        A function that extracts text chunks from a PDF file.
    chunk_size : int, optional
        The maximum size of each text chunk (default is 750).
    chunk_overlap : int, optional
        The overlap size between chunks (default is 500).

    Returns
    -------
    list
        A list of extracted document contents (each document's text content).
    """
    pdf_paths = Path(directory_path).glob("*.pdf")
    documents = []

    for pdf in pdf_paths:
        docs = extract_func(
            str(pdf), chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        documents.extend([doc.page_content for doc in docs if doc.page_content])

    return documents


def assemble_corpus(
    documents: list[str],
    seed_terms: list[str],
    ngram_range: tuple[int, int] = (1, 3),
    max_features: int = 1000,
    min_freq: int = 5,
) -> list[str]:
    """Assemble a corpus of terms.

    Parameters
    ----------
    documents : list
        A list of document text content.
    seed_terms : list
        A list of seed terms.
    ngram_range : tuple
        The range of n-grams to extract (default is unigrams to trigrams).
    max_features : int
        Maximum number of top terms to return.
    min_freq : int
        Minimum frequency threshold for n-grams to be considered.

    Returns
    -------
    list
        A list of the top graph theory-related terms.
    """
    lemmatizer = WordNetLemmatizer()

    stop_words = set(stopwords.words("english"))

    def preprocess_text(text: str) -> list[str]:
        text = unicodedata.normalize("NFKD", text)
        text = re.sub(r"[^\w\s]", " ", text.lower())
        tokens = word_tokenize(text)
        tagged_tokens = pos_tag(tokens)
        lemmatized_tokens = [
            lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag))
            for word, tag in tagged_tokens
            if word not in stop_words and word.isalpha() and len(word) >= 3
        ]
        return lemmatized_tokens

    def is_acronym(term: str) -> bool:
        return term.isupper()

    def get_wordnet_pos(treebank_tag):
        """Map POS tag to first character lemmatize() accepts"""
        if treebank_tag.startswith("J"):
            return "a"
        if treebank_tag.startswith("V"):
            return "v"
        if treebank_tag.startswith("N"):
            return "n"
        if treebank_tag.startswith("R"):
            return "r"
        return "n"

    processed_tokens = []
    for doc in documents:
        processed_tokens.extend(preprocess_text(doc))

    ngram_list = []
    for n in range(ngram_range[0], ngram_range[1] + 1):
        ngram_list.extend(ngrams(processed_tokens, n))

    ngram_counter = Counter(ngram_list)

    filtered_ngrams = [
        " ".join(ngram)
        for ngram, freq in ngram_counter.items()
        if freq >= min_freq and not is_acronym(" ".join(ngram))
    ]

    all_terms = set(filtered_ngrams).union(set(seed_terms))

    tfidf_vectorizer = TfidfVectorizer(
        max_features=max_features, ngram_range=(1, 3), stop_words="english"
    )
    tfidf_matrix = tfidf_vectorizer.fit_transform(list(all_terms))

    feature_scores = tfidf_matrix.sum(axis=0).A1
    feature_names = tfidf_vectorizer.get_feature_names_out()
    tfidf_scores = list(zip(feature_names, feature_scores))

    sorted_terms = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)

    top_terms = [term for term, score in sorted_terms[:max_features]]

    top_seed_terms = [term for term in seed_terms if term in top_terms]
    remaining_terms = [term for term in top_terms if term not in top_seed_terms]

    final_terms = top_seed_terms + remaining_terms

    logger.info(f"Extracted {len(final_terms)} graph theory terms.")

    return final_terms


def get_embedding(text, model):
    """Generate embeddings for the given text using the embedding model."""
    return model.encode(text, convert_to_tensor=True)


def filter_nodes_by_similarity(nodes, corpus_embeddings, model, threshold=0.6):
    """Filter nodes by calculating cosine similarity with the corpus embeddings.

    Parameters
    ----------
    nodes : list
        List of node dictionaries extracted by LLMGraphTransformer.
    corpus_embeddings : np.ndarray
        Precomputed embeddings for the graph theory corpus.
    model : SentenceTransformer
        The pre-trained SentenceTransformer model for embedding generation.
    threshold : float
        Similarity threshold for retaining nodes. Nodes with cosine similarity
        above this threshold are retained.

    Returns
    -------
    list
        List of filtered nodes.
    """
    filtered_nodes = []
    for node in nodes:
        node_embedding = get_embedding(node["name"], model)
        similarity_scores = cosine_similarity([node_embedding], corpus_embeddings)
        max_similarity = np.max(similarity_scores)
        if max_similarity > threshold:
            filtered_nodes.append(node)
    return filtered_nodes


def filter_relationships_by_similarity(
    relationships, corpus_embeddings, model, threshold=0.6
):
    """Filter relationships by calculating cosine similarity with the corpus embeddings.

    Parameters
    ----------
    relationships : list
        List of relationship dictionaries extracted by LLMGraphTransformer.
    corpus_embeddings : np.ndarray
        Precomputed embeddings for the graph theory corpus.
    model : SentenceTransformer
        The pre-trained SentenceTransformer model for embedding generation.
    threshold : float
        Similarity threshold for retaining relationships. Relationships with cosine
        similarity above this threshold are retained.

    Returns
    -------
    list
        List of filtered relationships.
    """
    filtered_relationships = []
    for relationship in relationships:
        relation_text = f"{relationship['source']} {relationship['relation']} "
        f"{relationship['target']}"
        relation_embedding = get_embedding(relation_text, model)
        similarity_scores = cosine_similarity([relation_embedding], corpus_embeddings)
        max_similarity = np.max(similarity_scores)
        if max_similarity > threshold:
            filtered_relationships.append(relationship)
    return filtered_relationships


def extract_text_by_chunk(
    doc_path: str,
    chunk_size: int = 10000,
    chunk_overlap: int = 750,
    noise_threshold: float = 0.1,
) -> list:
    def remove_exotic_characters(text: str) -> str:
        """Remove non-mathematical exotic characters from the text."""
        text = unicodedata.normalize("NFKD", text)

        allowed_ranges = [
            ("\u0030", "\u0039"),  # digits
            ("\u0041", "\u005a"),  # uppercase ASCII letters
            ("\u0061", "\u007a"),  # lowercase ASCII letters
            ("\u0020", "\u002f"),  # space and basic punctuation
            ("\u003a", "\u0040"),  # symbols like :, ;, <, =, >, ?, @
            ("\u005b", "\u0060"),  # brackets and backslash
            ("\u007b", "\u007e"),  # curly brackets and tilde
            (
                "\u00a0",
                "\u00ff",
            ),  # Latin-1 Supplement characters (for accented letters)
            ("\u2200", "\u22ff"),  # Mathematical operators
            ("\u2190", "\u21ff"),  # Arrows (used in LaTeX formulas)
            ("\u2100", "\u214f"),  # Additional letter-like symbols
        ]

        def is_allowed(char):
            return (
                any(start <= char <= end for start, end in allowed_ranges)
                or char.isascii()
                and char.isprintable()
            )

        return "".join(c for c in text if is_allowed(c))

    def is_dominated_by_repeated_patterns(
        text: str,
        patterns: list | None = None,
        threshold: float = 0.1,
    ) -> bool:
        """Check if the text is dominated by repeated patterns.

        Parameters
        ----------
        text : str
            The text to evaluate.
        patterns : list, optional
            A list of regex patterns to identify repeated sequences.
        threshold : float, optional
            The maximum allowed ratio of matched patterns to total text length, by
            default 0.1 (10%).

        Returns
        -------
        bool
            True if the text is dominated by repeated patterns, False otherwise.
        """
        if patterns is None:
            patterns = ["(?:\\s*\\.\\s*){5,}", "(?:\\b\\d+\\s+){15,}\\b"]
        matched_length = 0
        for pattern in patterns:
            matches = re.findall(pattern, text)
            matched_length += sum(len(match) for match in matches)
        total_length = len(text)
        if total_length == 0:
            return False
        ratio = matched_length / total_length
        logger.debug(f"Repeated patterns ratio: {ratio:.2f}")
        return ratio > threshold

    def insert_missing_spaces(text: str) -> str:
        """Insert missing spaces between concatenated words and handle common issues."""
        text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
        text = re.sub(r"(\w)-(\w)", r"\1 - \2", text)

        return text

    def clean_pdf_text(text: str) -> str:
        """Clean and normalize the extracted text using noise patterns."""
        text = re.sub(r"(?i)\bReferences\b.*", "", text, flags=re.DOTALL)
        text = re.sub(r"(?i)\bBibliography\b.*", "", text, flags=re.DOTALL)
        text = re.sub(r"(?i)\bWorks\s+Cited\b.*", "", text, flags=re.DOTALL)

        for pattern in NOISE_PATTERNS:
            text = re.sub(pattern, "", text, flags=re.MULTILINE)

        text = re.sub(r"\n\s*\n", "\n", text)
        text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
        text = re.sub(r"\s{2,}", " ", text)
        text = remove_exotic_characters(text)
        text = re.sub(r"\s+", " ", text).strip()
        text = re.sub(r"(?<=\s)\.\s+(?=[A-Z])", ". ", text)
        text = re.sub(r"\s*,\s*", ", ", text)
        text = re.sub(r"\s*\.\s*", ". ", text)
        text = re.sub(r"(\w)-(\w)", r"\1 - \2", text)  # Handle hyphenated words
        text = insert_missing_spaces(text)
        text = text.strip()
        return text

    try:
        loader = PyMuPDFLoader(doc_path)
        documents = loader.load()
        for doc in documents:
            if not doc.page_content:
                continue
            doc.page_content = clean_pdf_text(doc.page_content)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )
        chunks = text_splitter.split_documents(documents)
        chunks_filtered = [
            chunk
            for chunk in chunks
            if (
                len(chunk.page_content) > 500
                and not is_dominated_by_repeated_patterns(
                    chunk.page_content,
                    patterns=[r"(?:\s*\.\s*){5,}", r"(?:\b\d+\s+){15,}\b"],
                    threshold=noise_threshold,
                )
            )
        ]
    except Exception:
        logger.exception(f"Failed to process file {doc_path}")
        return []
    else:
        return chunks_filtered


def is_camel_case(term: str) -> bool:
    """Check if the given term is in camel case format."""
    return bool(re.search(r"[a-z]+[A-Z]", term))


def remove_stop_words(term: str) -> str:
    """Remove stop words from the term."""
    words = term.split()
    stop_words = set(stopwords.words("english"))
    return " ".join([word for word in words if word.lower() not in stop_words])


def save_corpus_as_txt(corpus: list[str], file_name: str) -> None:
    """Save the graph theory corpus as a text file inside the package data directory."""
    package_data_dir = get_package_data_directory()
    file_path = package_data_dir / file_name

    package_data_dir.mkdir(parents=True, exist_ok=True)

    with file_path.open("w") as txt_file:
        for term in corpus:
            txt_file.write(term + "\n")


def load_corpus(file_path: Path) -> list[str]:
    """Load a corpus from a text file. Each line in the text file represents one term
    or phrase.

    Parameters
    ----------
    file_path : Path
        Path to the text file containing terms.

    Returns
    -------
    List[str]
        A list of terms loaded from the file.
    """
    corpus = []
    file_path = Path(file_path)
    try:
        with file_path.open(encoding="utf-8") as file:
            for line in file:
                term = line.strip()
                if term:
                    corpus.append(term)
    except FileNotFoundError:
        logging.exception(f"File not found: {file_path}")
        return []
    except Exception:
        logging.exception(f"Error loading corpus from {file_path}")
        return []
    else:
        return corpus


def save_docs_to_jsonl(
    array: Iterable["Document"], file_name: str = "rag_documents.jsonl"
) -> None:
    """Save a list of Document objects to a JSONL file inside package data directory."""
    package_data_dir = get_package_data_directory()
    file_path = package_data_dir / file_name

    package_data_dir.mkdir(parents=True, exist_ok=True)

    with file_path.open("w") as jsonl_file:
        for doc in array:
            jsonl_file.write(doc.json() + "\n")


def load_docs_from_jsonl(file_path: Path) -> list["Document"]:
    """Load a list of Document objects from a JSONL file.

    Each line of the input file is deserialized from JSON format into a Document
    object, and the resulting objects are returned as a list.

    Parameters
    ----------
    file_path : Path
        The path to the input JSONL file from which documents will be loaded.

    Returns
    -------
    list of Document
        A list of Document objects loaded from the file.
    """
    file_path = Path(file_path)
    array = []
    with file_path.open() as jsonl_file:
        for line in jsonl_file:
            data = json.loads(line)
            obj = Document(**data)
            array.append(obj)
    return array
