from __future__ import annotations

import os
import subprocess
from pathlib import Path

from digitalhub.utils.exceptions import EntityError
from digitalhub.utils.logger import LOGGER

SKLEARN_RUNTIME = "mlserver_sklearn.SKLearnModel"
ENDPOINT = "http://localhost:8080/v2/models/model/infer"
FILENAME = "model-settings.json"
TEMPLATE = """
{{
    "name": "model",
    "implementation": "{}",
    "parameters": {{
        "uri": "{}"
    }}
}}
""".lstrip(
    "\n"
)


def serve_sklearn(root: Path) -> tuple:
    """
    Serve sklearn function.

    Parameters
    ----------
    root : Path
        The root path where config file is.

    Returns
    -------
    tuple
        Process ID and serving endpoint.
    """
    try:
        current_dir = os.getcwd()
        os.chdir(root)
        proc = subprocess.Popen(["mlserver", "start", "."])
        pid = proc.pid
        os.chdir(current_dir)
        return pid, ENDPOINT
    except Exception as e:
        msg = f"Something got wrong during sklearn serving. Exception: {e.__class__}. Error: {e.args}"
        LOGGER.exception(msg)
        raise EntityError(msg) from e


def config_sklearn(root: Path, model_path: str) -> None:
    """
    Configure sklearn function.

    Parameters
    ----------
    root : Path
        The root path where config file is.
    model_path : str
        The model path.

    Returns
    -------
    None
    """
    serving_json = TEMPLATE.format(SKLEARN_RUNTIME, model_path)
    (root / FILENAME).write_text(serving_json)
