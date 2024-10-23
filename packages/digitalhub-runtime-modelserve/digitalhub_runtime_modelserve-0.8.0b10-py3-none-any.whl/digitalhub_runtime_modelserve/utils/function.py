from __future__ import annotations

from typing import Callable

from digitalhub_runtime_modelserve.utils._registry import serve_function_registry

from digitalhub.utils.exceptions import EntityError
from digitalhub.utils.logger import LOGGER


def get_serve_function(action: str) -> Callable:
    """
    Get serve function.

    Parameters
    ----------
    action : str
        The action.

    Returns
    -------
    Callable
        The serve function.
    """
    try:
        return serve_function_registry[action]
    except KeyError as e:
        msg = f"Unsupported action {action} for local serving."
        LOGGER.error(msg)
        raise EntityError(msg) from e
    except Exception as e:
        msg = f"Something got wrong during function collection. Exception: {e.__class__}. Error: {e.args}"
        LOGGER.error(msg)
        raise EntityError(msg) from e
