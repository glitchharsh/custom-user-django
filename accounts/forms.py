from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UsernameOrEmailUser

class UsernameOrEmailUserCreationForm(UserCreationForm):

    class Meta:
        model = UsernameOrEmailUser
        fields = ("username", "email")

class UsernameOrEmailUserChangeForm(UserChangeForm):

    class Meta:
        model = UsernameOrEmailUser
        fields = ("username", "email")