from django.urls import path, include

from .views import UsernameOrEmailUserSignUpView, UsernameOrEmailUserLoginView

urlpatterns = [
    path('signup/', UsernameOrEmailUserSignUpView.as_view(), name='signup'),
    path('login/', UsernameOrEmailUserLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
]
