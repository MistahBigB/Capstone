from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('create/', TemplateView.as_view(template_name="index2.html"), name='create'),
    path('', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]
