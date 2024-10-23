import re
import bcrypt
from datetime import datetime
from django_dict_orm.exception import ValidationError

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


# Base Field class for different types of fields
class Field:
    def __init__(self, required=True, default=None):
        self.required = required
        self.default = default

    def validate(self, value):
        """Perform validation on field."""
        if self.required and value is None:
            raise ValidationError("This field is required.")

    def get_default(self):
        return self.default


# Specific field types
class IntegerField(Field):
    def validate(self, value):
        super().validate(value)
        if not isinstance(value, int):
            raise ValidationError(f"Expected an integer, got {type(value)} instead.")


class CharField(Field):
    def validate(self, value):
        super().validate(value)
        if not isinstance(value, str):
            raise ValidationError(f"Expected a string, got {type(value)} instead.")


class BooleanField(Field):
    def validate(self, value):
        super().validate(value)
        if not isinstance(value, bool):
            raise ValidationError(f"Expected a boolean, got {type(value)} instead.")


class EmailField(CharField):
    def validate(self, value):
        super().validate(value)
        if not re.match(EMAIL_REGEX, value):
            raise ValidationError(f"Invalid email format: {value}")


class FloatField(Field):
    def validate(self, value):
        super().validate(value)
        if not isinstance(value, float):
            raise ValidationError(f"Expected a float, got {type(value)} instead.")


class DateTimeField(Field):
    def __init__(self, auto_now_add=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_now_add = auto_now_add

    def get_default(self):
        if self.auto_now_add:
            return datetime.now().isoformat()
        return super().get_default()


class PasswordField(CharField):
    def hash_password(self, value):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(value.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
