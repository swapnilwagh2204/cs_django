from django import forms
from .models import Post, Tag


class PostsForm(forms.Form):
    tag = forms.MultipleChoiceField(
        choices=(('python', 'python'), ('adcanced', 'adcanced')))
    title = forms.CharField(max_length=40)
    slug = forms.CharField(max_length=30)
    content = forms.CharField(widget=forms.Textarea)


class postupdateform(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
