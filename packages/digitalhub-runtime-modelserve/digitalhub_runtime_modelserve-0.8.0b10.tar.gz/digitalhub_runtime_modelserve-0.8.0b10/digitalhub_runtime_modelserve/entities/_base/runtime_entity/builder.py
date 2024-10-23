from __future__ import annotations

from digitalhub.entities._base.runtime_entity.builder import RuntimeEntityBuilder


class RuntimeEntityBuilderMlflowserve(RuntimeEntityBuilder):
    EXECUTABLE_KIND = "mlflowserve"
    TASKS_KINDS = [
        {
            "kind": "mlflowserve+serve",
            "action": "serve",
        },
    ]
    RUN_KIND = "mlflowserve+run"


class RuntimeEntityBuilderSklearnserve(RuntimeEntityBuilder):
    EXECUTABLE_KIND = "sklearnserve"
    TASKS_KINDS = [
        {
            "kind": "sklearnserve+serve",
            "action": "serve",
        },
    ]
    RUN_KIND = "sklearnserve+run"


class RuntimeEntityBuilderHuggingfaceserve(RuntimeEntityBuilder):
    EXECUTABLE_KIND = "huggingfaceserve"
    TASKS_KINDS = [
        {
            "kind": "huggingfaceserve+serve",
            "action": "serve",
        },
    ]
    RUN_KIND = "huggingfaceserve+run"
