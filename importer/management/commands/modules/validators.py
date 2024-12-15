from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validateUrl(func):
    def inner(url):
        val = URLValidator()
        try:
            val(url)
        except ValidationError as e:
            raise ValidationError(e)
        else:
            return func(url)

    return inner
