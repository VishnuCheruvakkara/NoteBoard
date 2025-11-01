from django.urls import path 
from users.views import UserRegisterView, UserLoginView, UserLogoutView, LandingPageView
from notes.views import NoteListView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('dashboard/', NoteListView.as_view(), name='dashboard')
]