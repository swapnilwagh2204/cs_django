from django import forms
 
class studentform(forms.Form):
    name = forms.CharField(max_length=100)
    rn=forms.IntegerField()
    marks=forms.FloatField()


class postuserform(forms.Form):
    content =forms.CharField(max_length=1000)
    created_by=forms.CharField(max_length=100)
