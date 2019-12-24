from django.core.exceptions import ValidationError


def validate_date_format(date):
    digits = date.split('-')

    if len(digits) != 3:
        raise ValidationError(('Date format must be in YYYY-MM-DD'))

    if digits[0] < digits[1] or digits[0] < digits[2]:
        raise ValidationError(('Date format must be in YYYY-MM-DD'))

    if len(str(digits[0])) != 4:
        raise ValidationError(('Date format must be in YYYY-MM-DD'))

    if int(digits[1]) > 12 or int(digits[1]) < 1:
        raise ValidationError(('Date format must be in YYYY-MM-DD'))

    if int(digits[2]) > 31 or int(digits[2]) < 1:
        raise ValidationError(('Date format must be in YYYY-MM-DD'))
