import json
import logging
import random
import re
import textwrap
import warnings
from collections import Counter
from collections.abc import Callable
from typing import Any

import numpy as np
import torch

from nxlu.getters import get_supported_algorithms

warnings.filterwarnings("ignore")

logger = logging.getLogger("nxlu")

__all__ = [
    "sanitize_input",
    "most_common_element",
    "scrub_braces",
    "ReadableDict",
    "set_seed",
]


def sanitize_input(query: str) -> str:
    """Sanitize the user query by removing potentially harmful characters or patterns.

    Parameters
    ----------
    query : str
        The user's query.

    Returns
    -------
    str
        Sanitized query string.
    """
    return re.sub(r"[<>/]", "", query)


def most_common_element(elements: list[Any]) -> Any | None:
    """Return the most common element in a list or None if the list is empty.

    Parameters
    ----------
    elements : List[Any]
        The list of elements to evaluate.

    Returns
    -------
    Optional[Any]
        The most common element or None.
    """
    if not elements:
        return None
    return Counter(elements).most_common(1)[0][0]


def scrub_braces(context: Any) -> dict[str, Any]:
    """Recursively remove all instances of '{' and '}' from string-type values in the
    context dictionary.

    Parameters
    ----------
    context : Any
        The context dictionary to scrub. If not a dictionary, return an empty dict.

    Returns
    -------
    Dict[str, Any]
        The scrubbed context dictionary.
    """

    def scrub_value(value: Any) -> Any:
        if isinstance(value, str):
            value = re.sub(r"(?<!\{)\{(?!\{)", "", value)
            value = re.sub(r"(?<!\})\}(?!\})", "", value)
            return value
        if isinstance(value, dict):
            return {k: scrub_value(v) for k, v in value.items()}
        if isinstance(value, list):
            return [scrub_value(item) for item in value]
        if isinstance(value, tuple):
            return tuple(scrub_value(item) for item in value)
        if isinstance(value, set):
            return {scrub_value(item) for item in value}
        return value

    if not isinstance(context, dict):
        logger.warning(
            f"Invalid input to scrub_braces: {type(context)}. Returning empty dict."
        )
        return {}

    return {k: scrub_value(v) for k, v in context.items()}


class ReadableDict(dict):
    """A dictionary subclass that provides a more readable string representation
    with formatted output for nested dictionaries and long strings.

    Methods
    -------
    __str__():
        Return the formatted string representation of the dictionary.

    __repr__():
        Return the string representation (alias for __str__).

    _format_dict(d, indent=0):
        Recursively format the dictionary for a more readable output with
        indentation.

    _format_long_string(s, indent):
        Format long strings by wrapping text and maintaining indentation.
    """

    def __str__(self):
        """Return the formatted string representation of the dictionary."""
        return self._format_dict(self)

    def __repr__(self):
        """Return the string representation (alias for __str__)."""
        return self.__str__()

    def _format_dict(self, d, indent=0):
        """
        Recursively format the dictionary for a more readable output with
        indentation.

        Parameters
        ----------
        d : dict
            The dictionary to format.

        indent : int, optional
            The number of spaces to use for indentation (default is 0).

        Returns
        -------
        str
            The formatted dictionary as a string.
        """
        lines = ["{"]
        for key, value in d.items():
            if isinstance(value, dict):
                lines.append(
                    f"{' ' * (indent + 4)}'{key}': "
                    f"{self._format_dict(value, indent + 4)}"
                )
            elif isinstance(value, str) and "\n" in value:
                lines.append(f"{' ' * (indent + 4)}'{key}': '''")
                lines.extend(self._format_long_string(value, indent + 8))
                lines.append(f"{' ' * (indent + 4)}'''")
            elif isinstance(value, str):
                lines.append(f"{' ' * (indent + 4)}'{key}': {json.dumps(value)}")
            else:
                lines.append(f"{' ' * (indent + 4)}'{key}': {value!r}")
        lines.append(" " * indent + "}")
        return "\n".join(lines)

    def _format_long_string(self, s, indent):
        """
        Format long strings by wrapping text and maintaining indentation.

        Parameters
        ----------
        s : str
            The long string to format.

        indent : int
            The number of spaces to use for indentation.

        Returns
        -------
        list
            A list of formatted lines with appropriate indentation.
        """
        lines = []
        paragraphs = s.split("\n\n")
        for i, paragraph in enumerate(paragraphs):
            if i > 0:
                lines.append("")
            wrapped = textwrap.fill(
                paragraph,
                width=80,
                initial_indent=" " * indent,
                subsequent_indent=" " * indent,
            )
            lines.append(wrapped)
        return lines


def cosine_similarity(X: np.ndarray, Y: np.ndarray | None = None) -> np.ndarray:
    """
    Compute cosine similarity between samples in X and Y using pure numpy.

    Cosine similarity is the normalized dot product of X and Y:
        K(X, Y) = <X, Y> / (||X|| * ||Y||)

    Parameters
    ----------
    X : np.ndarray, shape (n_samples_X, n_features)
        Input data.

    Y : np.ndarray, shape (n_samples_Y, n_features), optional (default=None)
        Input data. If None, the output will be the pairwise
        similarities between all samples in X.

    Returns
    -------
    similarities : np.ndarray, shape (n_samples_X, n_samples_Y)
        Returns the cosine similarity between samples in X and Y.
    """
    if Y is None:
        Y = X

    # dot product between X and Y
    numerator = np.dot(X, Y.T)

    # L2 norms of each row in X and Y
    X_norms = np.linalg.norm(X, axis=1)
    Y_norms = np.linalg.norm(Y, axis=1)

    denominator = np.outer(X_norms, Y_norms)

    denominator[denominator == 0] = 1

    similarity = numerator / denominator

    return similarity


def set_seed(seed: int = 42):
    """Set the random seed for reproducibility."""
    random.seed(seed)
    np.random.default_rng(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def normalize_name(name: str) -> str:
    """Normalize the algorithm name by handling camel case and other formatting.

    Parameters
    ----------
    name : str
        The name to normalize.

    Returns
    -------
    str
        The normalized name.
    """
    name = re.sub(r"(?<!^)(?=[A-Z])", " ", name)
    name = name.lower()
    name = re.sub(r"[_\-]+", " ", name)
    name = re.sub(r"\s+", " ", name)
    name = name.replace("coefficient", "").replace("index", "")
    return name.strip()


def parse_algorithms(
    encyclopedia: dict, normalize_func: Callable
) -> tuple[list, dict, list]:
    """Load and normalize algorithm names from an encyclopedia.

    Parameters
    ----------
    encyclopedia : dict
        An algorithm encyclopedia dictionary.
    normalize_func : function
        A function that normalizes the algorithm names.

    Returns
    -------
    tuple
        A tuple containing:
        - A list of supported algorithms.
        - A dictionary mapping normalized algorithm names to their categories.
        - A list of the supported algorithms with standardized names.
    """
    supported_algorithms = get_supported_algorithms(encyclopedia)

    algorithm_categories = {
        normalize_func(alg).lower(): metadata.get("algorithm_category", "Unknown")
        for alg, metadata in encyclopedia.items()
    }

    standardized_names = list(algorithm_categories.keys())

    return supported_algorithms, algorithm_categories, standardized_names
