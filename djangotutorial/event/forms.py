from django import forms

class LoginForm(forms.Form):
    # customFields
    username = forms.CharField(label="Username", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))

