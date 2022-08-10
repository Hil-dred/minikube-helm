from cProfile import label
from django import forms

class Form(forms.Form):
    todo = forms.CharField(label='Enter Todo: ', max_length=50, required=True)