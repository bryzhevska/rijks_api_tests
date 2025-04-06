from pydantic import BaseModel, ValidationError


def validate_with_model(model: BaseModel, data: dict):
    try:
        return model.model_validate(data)
    except ValidationError as e:
        raise AssertionError(f"Validation failed: {e}")
