from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.EmailField(label='mail')
    age = forms.IntegerField(label='age')
