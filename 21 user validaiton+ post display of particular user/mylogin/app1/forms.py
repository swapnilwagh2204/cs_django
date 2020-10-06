from django import forms
from django.core.validators import ValidationError
from .validators import passwordvalidator,PasswordValidator,UsernameValidator

class postuserform(forms.Form):
    content= forms.CharField(max_length=100)
    created_by=forms.CharField(max_length=100)


class regForm(forms.Form):
    username = forms.CharField(validators=[UsernameValidator()])
    password = forms.CharField(validators=[PasswordValidator(8,20)])
    fullname = forms.CharField(max_length=100)
    address= forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=(('male','male'),('female','female')))
    