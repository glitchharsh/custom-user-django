from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsernameOrEmailUserCreationForm, UsernameOrEmailUserChangeForm
from .models import UsernameOrEmailUser

class UsernameOrEmailUserAdmin(UserAdmin):
    add_form = UsernameOrEmailUserCreationForm
    form = UsernameOrEmailUserChangeForm
    model = UsernameOrEmailUser
    list_display = ["email", "username",]

admin.site.register(UsernameOrEmailUser, UsernameOrEmailUserAdmin)
