from __future__ import annotations

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderMlflowserve
from digitalhub_runtime_modelserve.entities.run.mlflowserve_run.entity import RunMlflowserveRun
from digitalhub_runtime_modelserve.entities.run.mlflowserve_run.spec import (
    RunSpecMlflowserveRun,
    RunValidatorMlflowserveRun,
)
from digitalhub_runtime_modelserve.entities.run.mlflowserve_run.status import RunStatusMlflowserveRun

from digitalhub.entities.run._base.builder import RunBuilder


class RunMlflowserveRunBuilder(RunBuilder, RuntimeEntityBuilderMlflowserve):
    """
    RunMlflowserveRunBuilder runer.
    """

    ENTITY_CLASS = RunMlflowserveRun
    ENTITY_SPEC_CLASS = RunSpecMlflowserveRun
    ENTITY_SPEC_VALIDATOR = RunValidatorMlflowserveRun
    ENTITY_STATUS_CLASS = RunStatusMlflowserveRun
    ENTITY_KIND = "mlflowserve+run"
