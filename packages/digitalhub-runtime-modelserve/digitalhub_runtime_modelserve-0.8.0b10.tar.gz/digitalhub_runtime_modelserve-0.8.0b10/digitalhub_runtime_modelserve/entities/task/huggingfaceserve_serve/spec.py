from __future__ import annotations

from typing import Literal

from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import (
    TaskSpecModelserveServe,
    TaskValidatorModelserveServe,
)


class TaskSpecHuggingfaceserveServe(TaskSpecModelserveServe):
    """
    TaskSpecHuggingfaceserveServe specifications.
    """

    def __init__(
        self,
        function: str,
        node_selector: dict | None = None,
        volumes: list | None = None,
        resources: dict | None = None,
        affinity: dict | None = None,
        tolerations: list | None = None,
        envs: list | None = None,
        secrets: list | None = None,
        profile: str | None = None,
        huggingface_task_name: str | None = None,
        backend: str | None = None,
        tokenizer_revision: str | None = None,
        max_length: int | None = None,
        disable_lower_case: bool | None = None,
        disable_special_tokens: bool | None = None,
        dtype: str | None = None,
        trust_remote_code: bool | None = None,
        tensor_input_names: list[str] | None = None,
        return_token_type_ids: bool | None = None,
        return_probabilities: bool | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            function,
            node_selector,
            volumes,
            resources,
            affinity,
            tolerations,
            envs,
            secrets,
            profile,
            **kwargs,
        )

        self.huggingface_task_name = huggingface_task_name
        self.backend = backend
        self.tokenizer_revision = tokenizer_revision
        self.max_length = max_length
        self.disable_lower_case = disable_lower_case
        self.disable_special_tokens = disable_special_tokens
        self.dtype = dtype
        self.trust_remote_code = trust_remote_code
        self.tensor_input_names = tensor_input_names
        self.return_token_type_ids = return_token_type_ids
        self.return_probabilities = return_probabilities


class TaskValidatorHuggingfaceserveServe(TaskValidatorModelserveServe):
    """
    TaskValidatorHuggingfaceserveServe validator.
    """

    huggingface_task_name: Literal[
        "SEQUENCE_CLASSIFICATION",
        "TOKEN_CLASSIFICATION",
        "FILL_MASK",
        "TEXT_GENERATION",
        "TEXT2TEXT_GENERATION",
    ] = None
    """
    Huggingface task name.
    """

    backend: Literal["AUTO", "VLLM", "HUGGINGFACE"] = None
    """
    Backend type.
    """

    tokenizer_revision: str = None
    """
    Tokenizer revision.
    """

    max_length: int = None
    """
    Huggingface max sequence length for the tokenizer.
    """

    disable_lower_case: bool = None
    """
    Do not use lower case for the tokenizer.
    """

    disable_special_tokens: bool = None
    """
    The sequences will not be encoded with the special tokens relative to their model
    """

    dtype: Literal["AUTO", "FLOAT32", "FLOAT16", "BFLOAT16", "FLOAT", "HALF"] = None
    """
    Data type to load the weights in.
    """

    trust_remote_code: bool = None
    """
    Allow loading of models and tokenizers with custom code.
    """

    tensor_input_names: list[str] = None
    """
    The tensor input names passed to the model
    """

    return_token_type_ids: bool = None
    """
    Return token type ids
    """

    return_probabilities: bool = None
    """
    Return all probabilities
    """

    disable_log_requests: bool = None
    """
    Disable log requests
    """

    max_log_len: int = None
    """
    Max number of prompt characters or prompt
    """
