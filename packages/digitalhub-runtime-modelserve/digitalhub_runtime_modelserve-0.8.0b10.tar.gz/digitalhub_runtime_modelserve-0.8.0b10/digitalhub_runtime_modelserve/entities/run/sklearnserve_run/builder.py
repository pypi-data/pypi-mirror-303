from __future__ import annotations

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderSklearnserve
from digitalhub_runtime_modelserve.entities.run.sklearnserve_run.entity import RunSklearnserveRun
from digitalhub_runtime_modelserve.entities.run.sklearnserve_run.spec import (
    RunSpecSklearnserveRun,
    RunValidatorSklearnserveRun,
)
from digitalhub_runtime_modelserve.entities.run.sklearnserve_run.status import RunStatusSklearnserveRun

from digitalhub.entities.run._base.builder import RunBuilder


class RunSklearnserveRunBuilder(RunBuilder, RuntimeEntityBuilderSklearnserve):
    """
    RunSklearnserveRunBuilder runer.
    """

    ENTITY_CLASS = RunSklearnserveRun
    ENTITY_SPEC_CLASS = RunSpecSklearnserveRun
    ENTITY_SPEC_VALIDATOR = RunValidatorSklearnserveRun
    ENTITY_STATUS_CLASS = RunStatusSklearnserveRun
    ENTITY_KIND = "sklearnserve+run"
