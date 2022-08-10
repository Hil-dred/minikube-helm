from cProfile import label
from django import forms

class Auth(forms.Form):
    account_name = forms.CharField(label='Enter Account Name', max_length=20, required=False)
    master_password = forms.CharField(widget=forms.PasswordInput(), label='Enter Master Password', required=False)

class Form(forms.Form):
    app_name = forms.CharField(label='Enter Application Name e.g: DockerHub', max_length=20, required=False)
    user_name = forms.CharField(label='Enter User Name', max_length=20, required=False)
    password = forms.CharField(widget=forms.PasswordInput(), label='Enter Password', required=False)