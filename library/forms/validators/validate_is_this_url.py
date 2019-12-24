from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_is_this_url(string):
    validator = URLValidator()
    try:
        validator(string)
    except ValidationError:
        raise ValidationError(('This is not URL string'))
