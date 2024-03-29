from django import forms
from django.core import validators
from .validations import nameValidator, usernameValidator, emailValidator
from .models import registration, posts
import datetime
from django.contrib.auth.models import User


class UserForm(forms.Form):
    Name = forms.CharField(max_length=20, validators=[nameValidator])
    Email = forms.EmailField(validators=[emailValidator])
    Gender = forms.ChoiceField(
        choices=(('male', 'male'), ('female', 'female')))
    Username = forms.CharField(max_length=10, validators=[usernameValidator])
    Password = forms.CharField(max_length=10)


class PostsForm(forms.Form):
    # Author = forms.CharField(max_length=100)
    Title = forms.CharField(max_length=40)
    Content = forms.CharField(widget=forms.Textarea)
    # Date = forms.DateField(initial=datetime.date.today)


class postupdateform(forms.ModelForm):
    class Meta:
        model = posts
        exclude = ['author']
