from __future__ import annotations

from digitalhub_runtime_modelserve.utils._registry import config_function_registry

from digitalhub.utils.exceptions import EntityError
from digitalhub.utils.logger import LOGGER


def get_function_args(action: str, root: str, model_path: str) -> None:
    """
    Get function arguments.

    Parameters
    ----------
    action : str
        The action.
    root : str
        Root path.
    model_path : str
        The model path.

    Returns
    -------
    None
    """
    try:
        config_function_registry[action](root, model_path)
    except KeyError as e:
        msg = f"Unsupported action {action} for local serving."
        LOGGER.error(msg)
        raise EntityError(msg) from e
    except Exception as e:
        msg = f"Something got wrong during function configuration. Exception: {e.__class__}. Error: {e.args}"
        LOGGER.error(msg)
        raise EntityError(msg) from e
