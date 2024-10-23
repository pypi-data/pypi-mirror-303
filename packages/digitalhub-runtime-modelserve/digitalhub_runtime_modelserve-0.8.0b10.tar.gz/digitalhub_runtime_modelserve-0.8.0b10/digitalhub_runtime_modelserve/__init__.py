from __future__ import annotations

from digitalhub_runtime_modelserve.entities.function.huggingfaceserve.builder import FunctionHuggingfaceserveBuilder
from digitalhub_runtime_modelserve.entities.function.mlflowserve.builder import FunctionMlflowserveBuilder
from digitalhub_runtime_modelserve.entities.function.sklearnserve.builder import FunctionSklearnserveBuilder
from digitalhub_runtime_modelserve.entities.run.huggingfaceserve_run.builder import RunHuggingfaceserveRunBuilder
from digitalhub_runtime_modelserve.entities.run.mlflowserve_run.builder import RunMlflowserveRunBuilder
from digitalhub_runtime_modelserve.entities.run.sklearnserve_run.builder import RunSklearnserveRunBuilder
from digitalhub_runtime_modelserve.entities.task.huggingfaceserve_serve.builder import TaskHuggingfaceserveServeBuilder
from digitalhub_runtime_modelserve.entities.task.mlflowserve_serve.builder import TaskMlflowserveServeBuilder
from digitalhub_runtime_modelserve.entities.task.sklearnserve_serve.builder import TaskSklearnserveServeBuilder

entity_builders = (
    (FunctionHuggingfaceserveBuilder.ENTITY_KIND, FunctionHuggingfaceserveBuilder),
    (FunctionMlflowserveBuilder.ENTITY_KIND, FunctionMlflowserveBuilder),
    (FunctionSklearnserveBuilder.ENTITY_KIND, FunctionSklearnserveBuilder),
    (TaskHuggingfaceserveServeBuilder.ENTITY_KIND, TaskHuggingfaceserveServeBuilder),
    (TaskMlflowserveServeBuilder.ENTITY_KIND, TaskMlflowserveServeBuilder),
    (TaskSklearnserveServeBuilder.ENTITY_KIND, TaskSklearnserveServeBuilder),
    (RunHuggingfaceserveRunBuilder.ENTITY_KIND, RunHuggingfaceserveRunBuilder),
    (RunMlflowserveRunBuilder.ENTITY_KIND, RunMlflowserveRunBuilder),
    (RunSklearnserveRunBuilder.ENTITY_KIND, RunSklearnserveRunBuilder),
)

try:
    from digitalhub_runtime_modelserve.runtimes.builder import RuntimeModelserveBuilder

    runtime_builders = (
        *[(kind, RuntimeModelserveBuilder) for kind in FunctionSklearnserveBuilder().get_all_kinds()],
        *[(kind, RuntimeModelserveBuilder) for kind in FunctionMlflowserveBuilder().get_all_kinds()],
        *[(kind, RuntimeModelserveBuilder) for kind in FunctionHuggingfaceserveBuilder().get_all_kinds()],
    )
except ImportError:
    runtime_builders = tuple()
