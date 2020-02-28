from django.urls import path, include
from . import views
from django.shortcuts import redirect
from django.views.generic.base import TemplateView # new

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', lambda request: redirect('accounts/login', permanent=False)),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home', TemplateView.as_view(template_name='home.html'), name='home'), # new
]
