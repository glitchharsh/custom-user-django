from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='welcome', permanent=False)),
    path('welcome/', TemplateView.as_view(template_name='welcome.html'), name='welcome'),
    path('accounts/', include('accounts.urls')),
]
