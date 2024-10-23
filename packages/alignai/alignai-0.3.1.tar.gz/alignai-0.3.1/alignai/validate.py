class ValidationError(ValueError):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"ValidationError: {self.message}"


def validate_session_id_or_raise(session_id: str):
    if not session_id:
        raise ValidationError("session_id is required")
    if len(session_id) > 64:
        raise ValidationError("session_id must be at most 64 characters")


def validate_user_id_or_raise(user_id: str):
    if not user_id:
        raise ValidationError("user_id is required")
    if len(user_id) > 64:
        raise ValidationError("user_id must be at most 64 characters")


def validate_custom_properties_or_raise(custom_properties: dict[str, str]):
    if len(custom_properties) > 10:
        raise ValidationError("custom_properties must have at most 10 keys")
    for key, value in custom_properties.items():
        if not key:
            raise ValidationError("key of custom_property is required")
        if len(key) > 64:
            raise ValidationError("key of custom_property must be at most 64 characters")
        if len(value) > 256:
            raise ValidationError("value of custom_property must be at most 256 characters")
