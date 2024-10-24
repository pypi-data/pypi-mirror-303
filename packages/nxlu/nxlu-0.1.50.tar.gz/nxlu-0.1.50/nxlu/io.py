import importlib.resources as importlib_resources
import json
import logging
import warnings
from typing import Any

warnings.filterwarnings("ignore")


logger = logging.getLogger("nxlu")

__all__ = [
    "load_algorithm_encyclopedia",
    "load_algorithm_docs",
]


def load_algorithm_encyclopedia() -> dict[str, dict[str, Any]]:
    """Load the encyclopedia of algorithm applicability conditions from a JSON file.

    Returns
    -------
    Dict[str, Dict[str, Any]]
        Dictionary containing algorithm applicability conditions.
    """
    try:
        with importlib_resources.open_text(
            "nxlu.data", "algorithm_encyclopedia.json"
        ) as file:
            applicability = json.load(file)
    except FileNotFoundError:
        error_message = "Algorithm encyclopedia file not found."
        logger.exception(error_message)
        raise FileNotFoundError(error_message)
    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON: {e}"
        logger.exception(error_message)
        raise ValueError(error_message)
    else:
        logger.info("Loaded algorithm encyclopedia successfully.")
        return applicability


def load_algorithm_docs(algorithm_name: str | None = None) -> dict | None:
    """Load algorithm documentation from a JSON file using pathlib.

    Returns
    -------
    dict | None
        Dictionary containing algorithm documentation.
    """
    try:
        with importlib_resources.open_text("nxlu.data", "algorithm_docs.json") as file:
            alg_docs = json.load(file)
    except FileNotFoundError:
        error_message = "Algorithm documentation file not found."
        logger.exception(error_message)
        raise FileNotFoundError(error_message)
    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON: {e}"
        logger.exception(error_message)
        raise ValueError(error_message)
    else:
        logger.info("Loaded algorithm documentation successfully.")
        if algorithm_name:
            if algorithm_name in list(alg_docs.keys()):
                return alg_docs[algorithm_name]
            return None
        return alg_docs
