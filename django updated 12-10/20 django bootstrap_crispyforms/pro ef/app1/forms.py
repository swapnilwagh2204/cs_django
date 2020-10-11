from django import forms
from django.db.models import fields
from . models import student

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"
        # fields=("subject",'school','marks')  #je aplyala paije te field havyat tr
        # exclude =['marks','name','school']  # ji field paije nai te hyat takaychya


