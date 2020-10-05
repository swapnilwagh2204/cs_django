import re
from django import forms
from django.core import validators
class empform(forms.Form):
    username = forms.CharField(validators=[validators.MinLengthValidator(8),validators.MaxLengthValidator(20)])
    
    password = forms.CharField(validators=[validators.MinLengthValidator(8),validators.MaxLengthValidator(20)])
    '''
    def clean_username(self):
        uname=self.cleaned_data['username']
        print("entered name--->",uname)
        if len(uname)<8:
            raise forms.ValidationError("Invalid name !!! name should be at least 5 characters")
        else:
            newval=uname.upper()
            return newval
    '''
    def clean_password(self):
        passwd=self.cleaned_data['password']
        print("entered name--->",passwd)
        if len(passwd)<8:
            raise forms.ValidationError("Invalid password !!! password should be at least 8 characters")
        if not re.findall('\d', passwd):
            raise forms.ValidationError("password must contain one digit")
        
        if not re.findall('[A-Z]', passwd):
            raise forms.ValidationError("The password must contain at least 1 uppercase letter, A-Z.")

        if not re.findall('[a-z]', passwd):
            raise forms.ValidationError("The password must contain at least 1 lowercase letter, a-z.")
                

        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', passwd):
            raise forms.ValidationError("The password must contain at least 1 symbol: " +
                    "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?")
        
        else:
            return passwd
    
