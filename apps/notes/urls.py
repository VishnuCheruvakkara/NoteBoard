from django.urls import path
from notes.views import NoteCreateView,NoteListView, NoteDetailView, NoteUpdateView


urlpatterns = [
    path('create/', NoteCreateView.as_view(), name='create'),
    path('list/', NoteListView.as_view(), name='list'),
    path('<int:pk>/', NoteDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', NoteUpdateView.as_view(), name='edit'),
]
