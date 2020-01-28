from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('create/', TemplateView.as_view(template_name="index2.html"), name='create'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('signup/', views.SignUp.as_view(), name='signup'),
]
