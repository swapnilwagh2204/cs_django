from django import forms
from .models import File  # models.py


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["name", "filepath"]
