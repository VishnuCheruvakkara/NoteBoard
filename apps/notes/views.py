from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from notes.models import Note 
from notes.forms import NoteForm 

# Create your views here.
class NoteCreateView(LoginRequiredMixin, CreateView):
    model= Note 
    form_class=NoteForm 
    template_name = 'dashboard/dashboard.html' 
    success_url=reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user=self.request.user 
        return super().form_valid(form)
    
