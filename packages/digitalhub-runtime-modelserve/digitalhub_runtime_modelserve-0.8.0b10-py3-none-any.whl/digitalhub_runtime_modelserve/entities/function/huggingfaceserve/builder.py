from __future__ import annotations

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderHuggingfaceserve
from digitalhub_runtime_modelserve.entities.function.huggingfaceserve.entity import FunctionHuggingfaceserve
from digitalhub_runtime_modelserve.entities.function.huggingfaceserve.spec import (
    FunctionSpecHuggingfaceserve,
    FunctionValidatorHuggingfaceserve,
)
from digitalhub_runtime_modelserve.entities.function.huggingfaceserve.status import FunctionStatusHuggingfaceserve

from digitalhub.entities.function._base.builder import FunctionBuilder


class FunctionHuggingfaceserveBuilder(FunctionBuilder, RuntimeEntityBuilderHuggingfaceserve):
    """
    FunctionHuggingfaceserve builder.
    """

    ENTITY_CLASS = FunctionHuggingfaceserve
    ENTITY_SPEC_CLASS = FunctionSpecHuggingfaceserve
    ENTITY_SPEC_VALIDATOR = FunctionValidatorHuggingfaceserve
    ENTITY_STATUS_CLASS = FunctionStatusHuggingfaceserve
    ENTITY_KIND = "huggingfaceserve"
