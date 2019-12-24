from django.core.exceptions import ValidationError


def validate_page_count(page_count):
    if type(page_count) != str:
        raise ValidationError(('this is not a string'))

    if not int(page_count) > 0:
        raise ValidationError(('page_count cannot be smaller than 0'))
