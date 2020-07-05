from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2, max_length=20)
    password = forms.CharField(required=True, min_length=6, max_length=12)
