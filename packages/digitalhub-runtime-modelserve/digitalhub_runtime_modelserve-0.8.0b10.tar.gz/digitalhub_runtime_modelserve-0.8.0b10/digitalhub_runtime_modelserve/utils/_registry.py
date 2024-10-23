from __future__ import annotations

serve_function_registry = {}
config_function_registry = {}

try:
    from digitalhub_runtime_modelserve.utils.frameworks.sklearn import config_sklearn, serve_sklearn

    serve_function_registry["sklearnserve+serve"] = serve_sklearn
    config_function_registry["sklearnserve+serve"] = config_sklearn
except ImportError:
    ...

try:
    from digitalhub_runtime_modelserve.utils.frameworks.mlflow import config_mlflow, serve_mlflow

    serve_function_registry["mlflowserve+serve"] = serve_mlflow
    config_function_registry["mlflowserve+serve"] = config_mlflow
except ImportError:
    ...
