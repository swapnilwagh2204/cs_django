from django import forms
from django.core import validators
class studentform(forms.Form):
    name = forms.CharField(max_length=100)
    rn=forms.IntegerField(validators=[validators.MinValueValidator(1),validators.MaxValueValidator(20)])
    marks=forms.FloatField(validators=[validators.MaxValueValidator(100)])

    def clean_name(self):
        entered_name=self.cleaned_data['name']
        print("entered name--->",entered_name)
        if len(entered_name)<3:
            raise forms.ValidationError("Invalid name !!! name should be at least 5 characters")
        else:
            newval=entered_name.upper()
            return newval

class postuserform(forms.Form):
    content =forms.CharField(max_length=1000)
    created_by=forms.CharField(max_length=100)
