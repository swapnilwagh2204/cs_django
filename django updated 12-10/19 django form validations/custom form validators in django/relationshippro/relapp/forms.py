from django import forms
from django.core.validators import ValidationError
from .validators import passwordvalidator,PasswordValidator,UsernameValidator




class EmpForm(forms.Form):
    username = forms.CharField(validators=[UsernameValidator()])
    password = forms.CharField(validators=[PasswordValidator(8,20)])
    fullname = forms.CharField()
    address = forms.CharField()
    gender = forms.ChoiceField(choices=(('male','male'),('female','female')))
    city = forms.CharField()