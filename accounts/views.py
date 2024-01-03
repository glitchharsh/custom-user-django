from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model

from .forms import UsernameOrEmailUserCreationForm, UsernameOrEmailUserLoginForm

class UsernameOrEmailUserLoginView(LoginView):
    form_class = UsernameOrEmailUserLoginForm
    template_name = 'registration/login.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username')
        if '@' in username:
            username_qs = get_user_model().objects.filter(email = username)
            if len(username) != 0:
                username = username_qs.first().username
                request.POST._mutable = True
                request.POST['username'] = username
                request.POST._mutable = False
        return super(LoginView, self).post(request, kwargs)


class UsernameOrEmailUserSignUpView(CreateView):
    form_class = UsernameOrEmailUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
