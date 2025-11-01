from django.urls import path
from notes.views import NoteCreateView


urlpatterns = [
    path('create/', NoteCreateView.as_view(), name='create'),
 
]
