from __future__ import annotations

import os
import subprocess
from pathlib import Path

from digitalhub.utils.exceptions import EntityError
from digitalhub.utils.logger import LOGGER

MLFLOW_RUNTIME = "mlserver_mlflow.MLflowRuntime"
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


def serve_mlflow(root: Path) -> tuple:
    """
    Serve mlflow function.

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
        msg = f"Something got wrong during mlflow serving. Exception: {e.__class__}. Error: {e.args}"
        LOGGER.exception(msg)
        raise EntityError(msg) from e


def config_mlflow(root: Path, model_path: str) -> None:
    """
    Configure mlflow function.

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
    if model_path.endswith("MLmodel"):
        model_path = model_path.removesuffix("MLmodel")
    serving_json = TEMPLATE.format(MLFLOW_RUNTIME, model_path)
    (root / FILENAME).write_text(serving_json)
