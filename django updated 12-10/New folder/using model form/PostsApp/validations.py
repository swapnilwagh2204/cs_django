from django.core.validators import ValidationError
from .models import registration


def nameValidator(value):
    if len(value) <= 2 or len(value) > 10:
        raise ValidationError('Enter valid name')
    return value


def usernameValidator(value):
    if registration.objects.filter(username=value):
        raise ValidationError('Username already exists!!')
    return value


def emailValidator(value):
    if registration.objects.filter(email=value):
        raise ValidationError('email already exists!! Please Login...')
    return value
