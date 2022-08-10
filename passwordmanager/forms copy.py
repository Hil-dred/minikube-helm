from django import forms

class PasswordForm(forms.Form):
    master_password = forms.CharField(label='Master Password', max_length=100, required=False)