from django.urls import path, include

from .views import UsernameOrEmailUserSignUpView, UsernameOrEmailUserLoginView, ProfileView

urlpatterns = [
    path('signup/', UsernameOrEmailUserSignUpView.as_view(), name='signup'),
    path('login/', UsernameOrEmailUserLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include('django.contrib.auth.urls')),
]
