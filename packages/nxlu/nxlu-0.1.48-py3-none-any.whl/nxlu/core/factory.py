import importlib.metadata
import logging

from nxlu.core.base import BaseBackend
from nxlu.exceptions import raise_backend_key_error

logger = logging.getLogger("nxlu")


__all__ = ["get_backend"]


def get_backend(backend_name: str) -> BaseBackend:
    """Retrieve a backend instance based on the backend name.

    Parameters
    ----------
    backend_name : str
        The name of the backend to instantiate.

    Returns
    -------
    BaseBackend
        An instance of a backend implementing BaseBackend.

    Raises
    ------
    ValueError
        If the specified backend is not registered.
    """
    try:
        entry_points = importlib.metadata.entry_points()
        # Python >=3.10
        backend_entry_points = entry_points.select(
            group="networkx.backends", name=backend_name
        )
        if not backend_entry_points:
            raise_backend_key_error(backend_name)
        entry_point = backend_entry_points.pop()
        backend_class = entry_point.load()
        logger.info(f"Selected backend '{backend_name}'.")
        return backend_class()
    except (IndexError, KeyError, AttributeError):
        # Python <3.10, where `select` is not available
        entry_points = importlib.metadata.entry_points()
        backend_entry_points = [
            ep
            for ep in entry_points
            if ep.group == "networkx.backends" and ep.name == backend_name
        ]
        if backend_entry_points:
            entry_point = backend_entry_points[0]
            backend_class = entry_point.load()
            logger.info(f"Selected backend '{backend_name}'.")
            return backend_class()
        available_backends = [
            ep.name
            for ep in importlib.metadata.entry_points()
            if ep.group == "networkx.backends"
        ]
        error_msg = f"Backend '{backend_name}' is not registered. Available backends: "
        f"{available_backends}"
        logger.exception(error_msg)
        raise ValueError(error_msg)
