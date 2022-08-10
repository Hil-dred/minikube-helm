from django import forms

class PasswordForm(forms.Form):
    account_name = forms.CharField(label='Master Password', max_length=100, required=False)
    master_password = forms.CharField(label='Master Password', max_length=100, required=False)