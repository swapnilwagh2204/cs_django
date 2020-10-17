from django import forms
from django.core.validators import ValidationError
from .models import Post
from django.forms import Form

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','password1','password2','email','first_name','last_name']


class PostModelForm(forms.Form):
    tag = forms.CharField()
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)


class PostModelForm1(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


