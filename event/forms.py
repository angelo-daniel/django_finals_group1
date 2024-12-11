from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    # customFields
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control shadow-sm rounded font-light',
                'placeholder': 'Enter your username',
                'style': 'border: 1px solid #ced4da; padding: 10px;'
            }

        )
    )
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control shadow-sm rounded font-light',
                'placeholder': 'Enter your password',
                'style': 'border: 1px solid #ced4da; padding: 10px;'
            }
        )
    )

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email Address",
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control shadow-sm rounded font-light',
                'placeholder': 'Enter your email',
                'style': 'border: 1px solid #ced4da; padding: 10px;'
            }
        )
    )
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control shadow-sm rounded font-light',
                'placeholder': 'Enter your username',
                'style': 'border: 1px solid #ced4da; padding: 10px;'
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control shadow-sm rounded font-light',
                'placeholder': 'Enter your password',
                'style': 'border: 1px solid #ced4da; padding: 10px;'
            }
        )
    )
    password2 = forms.CharField(
        label=" Confirm",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control shadow-sm rounded font-light',
                'placeholder': 'Confirm your password',
                'style': 'border: 1px solid #ced4da; padding: 10px;'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
