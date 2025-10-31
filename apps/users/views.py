from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import RegisterForm 
from users.models import CustomUser 


import logging 

logger = logging.getLogger(__name__)

# Create your views here.
class LandingPageView(TemplateView):
    template_name='landing/landing.html'

class UserRegisterView(CreateView):
    model= CustomUser 
    form_class = RegisterForm 
    template_name='users/register.html'
    success_url = reverse_lazy('dashboard')

class UserLoginView(LoginView):
    pass 

class UserLogoutView(LogoutView):
    pass