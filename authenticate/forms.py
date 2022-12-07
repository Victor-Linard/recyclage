from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self)
        self.fields["username"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields["password1"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your password'})
        self.fields["password2"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})

        class Meta(UserCreationForm.Meta):
            model = get_user_model()
            fields = ('username', 'password1', 'password2')


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Nom d’utilisateur')

    password = forms.CharField(
        max_length=63,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
        label='Mot de passe')