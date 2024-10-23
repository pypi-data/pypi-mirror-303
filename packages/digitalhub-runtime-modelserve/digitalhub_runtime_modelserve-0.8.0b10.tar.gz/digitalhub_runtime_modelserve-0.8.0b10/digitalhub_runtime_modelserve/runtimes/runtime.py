from __future__ import annotations

from typing import Callable

from digitalhub_runtime_modelserve.utils.configuration import get_function_args
from digitalhub_runtime_modelserve.utils.function import get_serve_function

from digitalhub.context.api import get_context
from digitalhub.runtimes._base import Runtime
from digitalhub.utils.logger import LOGGER


class RuntimeModelserve(Runtime):
    """
    Runtime Model Serve base class.
    """

    def __init__(self, project: str) -> None:
        super().__init__(project)
        ctx = get_context(self.project)
        self.root = ctx.root

    def build(self, function: dict, task: dict, run: dict) -> dict:
        """
        Build run spec.

        Parameters
        ----------
        function : dict
            The function.
        task : dict
            The task.
        run : dict
            The run.

        Returns
        -------
        dict
            The run spec.
        """
        return {
            **function.get("spec", {}),
            **task.get("spec", {}),
            **run.get("spec", {}),
        }

    def run(self, run: dict) -> dict:
        """
        Run function.

        Returns
        -------
        dict
            Status of the executed run.
        """
        raise NotImplementedError("Local execution not implemented.")
        LOGGER.info("Validating task.")
        self._validate_task(run)

        LOGGER.info("Starting task.")
        spec = run.get("spec")

        task_kind = run["spec"]["task"].split(":")[0]
        LOGGER.info(f"Get executable for {task_kind}.")
        executable = self._get_executable(task_kind)

        LOGGER.info("Configure execution.")
        self._configure_execution(task_kind, self.root, spec.get("path"))

        LOGGER.info("Serve model.")
        pid, endpoint = self._execute(executable, self.root)

        LOGGER.info("Task completed, returning run status.")
        return {"results": {"endpoint": endpoint, "pid": pid}}

    @staticmethod
    def _get_executable(action: str) -> Callable:
        """
        Select function according to action.

        Parameters
        ----------
        action : str
            Action to execute.

        Returns
        -------
        Callable
            Function to execute.
        """
        return get_serve_function(action)

    @staticmethod
    def _configure_execution(action: str, root: str, model_path: str) -> None:
        """
        Configure execution.

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
        return get_function_args(action, root, model_path)
