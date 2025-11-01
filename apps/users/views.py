from django.shortcuts import render,redirect
from django.urls import reverse_lazy 
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import RegisterForm,LoginForm
from users.models import CustomUser 
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from users.mixins import RedirectAuthenticatedUserMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from notes.forms import NoteForm

import logging 

logger = logging.getLogger(__name__)

# Create your views here.
@method_decorator(never_cache, name='dispatch')
class LandingPageView(RedirectAuthenticatedUserMixin,TemplateView):
    template_name='landing/landing.html'

@method_decorator(never_cache, name='dispatch')
class UserRegisterView(RedirectAuthenticatedUserMixin,CreateView):
    model= CustomUser 
    form_class = RegisterForm 
    template_name='users/register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f"Welcome {user.username}, your account has been created successfully!")
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below and try again.")
        return super().form_invalid(form)

@method_decorator(never_cache, name='dispatch')
class UserLoginView(RedirectAuthenticatedUserMixin,LoginView):
    template_name='users/login.html'
    form_class=LoginForm
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('dashboard')
    
    def form_valid(self, form):
        messages.success(self.request, "Welcome back!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid email or password. Please try again.")
        return super().form_invalid(form)

class UserLogoutView(LogoutView):
    next_page=reverse_lazy('landing_page')

class DashBoardView(LoginRequiredMixin,TemplateView):
    template_name='dashboard/dashboard.html'
    login_url=reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NoteForm()  #  Pass the form to template
        return context