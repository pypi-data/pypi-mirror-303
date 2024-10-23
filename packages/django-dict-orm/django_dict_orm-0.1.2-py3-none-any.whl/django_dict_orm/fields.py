import re
import bcrypt
from datetime import datetime
from decimal import Decimal
from django_dict_orm.exception import ValidationError

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


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


class IntegerField(Field):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        super().validate(value)
        if not isinstance(value, int):
            raise ValidationError(f"Expected an integer, got {type(value)} instead.")
        if self.min_value is not None and value < self.min_value:
            raise ValidationError(f"Value {value} is less than minimum value {self.min_value}.")
        if self.max_value is not None and value > self.max_value:
            raise ValidationError(f"Value {value} is greater than maximum value {self.max_value}.")


class CharField(Field):
    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_length = max_length
        self.min_length = min_length

    def validate(self, value):
        super().validate(value)
        if not isinstance(value, str):
            raise ValidationError(f"Expected a string, got {type(value)} instead.")
        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(f"Value exceeds max_length of {self.max_length}.")
        if self.min_length is not None and len(value) < self.min_length:
            raise ValidationError(f"Value is shorter than min_length of {self.min_length}.")


class TextField(CharField):
    pass  # Same as CharField, but typically used for larger bodies of text.


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


class DecimalField(Field):
    def __init__(self, max_digits=None, decimal_places=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_digits = max_digits
        self.decimal_places = decimal_places

    def validate(self, value):
        super().validate(value)
        if not isinstance(value, Decimal):
            raise ValidationError(f"Expected a Decimal, got {type(value)} instead.")
        if self.max_digits is not None and len(str(value).replace('.', '')) > self.max_digits:
            raise ValidationError(f"Value exceeds max_digits of {self.max_digits}.")
        if self.decimal_places is not None and len(str(value).split('.')[-1]) > self.decimal_places:
            raise ValidationError(f"Value exceeds decimal_places of {self.decimal_places}.")


class DateTimeField(Field):
    def __init__(self, auto_now_add=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_now_add = auto_now_add

    def get_default(self):
        if self.auto_now_add:
            return datetime.now().isoformat()
        return super().get_default()


class URLField(CharField):
    URL_REGEX = r'^https?://[^\s]+$'

    def validate(self, value):
        super().validate(value)
        if not re.match(self.URL_REGEX, value):
            raise ValidationError(f"Invalid URL format: {value}")


class PasswordField(CharField):
    def hash_password(self, value):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(value.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
