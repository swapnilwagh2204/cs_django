from django import forms
from django.core.validators import ValidationError
from .validators import PasswordValidator, UsernameValidator


class postuserform(forms.Form):
    content = forms.CharField(max_length=100)
    created_by = forms.CharField(max_length=100)


class regForm(forms.Form):
    username = forms.CharField(validators=[UsernameValidator()])
    password = forms.CharField(validators=[PasswordValidator(8, 20)])
    fullname = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    gender = forms.ChoiceField(
        choices=(('male', 'male'), ('female', 'female')))

    def clean_username(self):
        uname = self.cleaned_data['username']
        print("entered name--->", uname)
        if len(uname) < 8:
            raise forms.ValidationError(
                "Invalid name !!! name should be at least 8 characters")
        else:
            newval = uname.upper()
            return newval
