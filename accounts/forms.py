from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms

from .models import UsernameOrEmailUser

class UsernameOrEmailUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

class UsernameOrEmailUserCreationForm(UserCreationForm):

    class Meta:
        model = UsernameOrEmailUser
        fields = ("username", "email")

class UsernameOrEmailUserChangeForm(UserChangeForm):

    class Meta:
        model = UsernameOrEmailUser
        fields = ("username", "email")