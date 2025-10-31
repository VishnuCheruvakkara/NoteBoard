from django.urls import path 
from .views import UserRegisterView, UserLoginView, UserLogoutView, LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]