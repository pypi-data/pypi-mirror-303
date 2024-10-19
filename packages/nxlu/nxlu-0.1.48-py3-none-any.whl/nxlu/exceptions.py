import logging
import warnings

warnings.filterwarnings("ignore")

logger = logging.getLogger("nxlu")

__all__ = ["handle_error"]


def handle_error(e: Exception, message: str = "An error occurred") -> None:
    """Log an error message along with the exception details.

    Parameters
    ----------
    e : Exception
        The exception that was raised.
    message : str, optional
        A custom error message, by default "An error occurred".

    Returns
    -------
    None
    """
    logger.error(f"{message}: {e}")


def raise_backend_key_error(backend_name: str) -> None:
    """Raise a key error if the backend name is not found in the pyproject.toml"""
    raise KeyError(f"Backend '{backend_name}' not found in entry points.")
