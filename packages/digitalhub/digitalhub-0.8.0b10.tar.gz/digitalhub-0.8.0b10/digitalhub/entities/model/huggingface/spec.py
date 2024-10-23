from __future__ import annotations

from digitalhub.entities.model._base.spec import ModelSpec, ModelValidator


class ModelSpecHuggingface(ModelSpec):
    """
    ModelSpecHuggingface specifications.
    """

    def __init__(
        self,
        path: str,
        framework: str | None = None,
        algorithm: str | None = None,
        base_model: str | None = None,
        parameters: dict | None = None,
        metrics: dict | None = None,
        model_id: str | None = None,
        model_revision: str = None,
    ) -> None:
        super().__init__(path, framework, algorithm, base_model, parameters, metrics)
        self.model_id = model_id
        self.model_revision = model_revision


class ModelValidatorHuggingface(ModelValidator):
    """
    ModelValidatorHuggingface validator.
    """

    model_id: str = None
    """Huggingface model id. If not specified, the model is loaded from the model path."""

    model_revision: str = None
    """Huggingface model revision."""
