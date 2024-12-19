"""
Validators
"""

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(func):
    """
    Decorator for validating url.
    """
    def inner(url):
        val = URLValidator()
        try:
            val(url)
        except ValidationError as e:
            raise ValidationError(e) from e

        return func(url)

    return inner
