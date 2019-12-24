from django.core.exceptions import ValidationError


def validate_isbn(isbn):
    if type(isbn) != str:
        raise ValidationError(('this is not a string'))
    if len(isbn) != 13:
        raise ValidationError(('ISBN must have 13 digits'))

    if not isbn.isdigit():
        raise ValidationError(('ISBN cannot have letters'))
