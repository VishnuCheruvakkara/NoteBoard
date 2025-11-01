from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from notes.models import Note 
from notes.forms import NoteForm 
from django.db.models import Q
# Create your views here.
class NoteCreateView(LoginRequiredMixin, CreateView):
    model= Note 
    form_class=NoteForm 
    template_name = 'dashboard/dashboard.html' 
    success_url=reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user=self.request.user 
        return super().form_valid(form)
    
class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'notes'
    paginate_by = 8
    login_url = reverse_lazy('login')

    def get_queryset(self):
        qs = Note.active_notes.filter(user=self.request.user)
        query = self.request.GET.get('q', '')
        if query:
            qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NoteForm()  # for the modal form
        return context

class NoteDetailView(LoginRequiredMixin, DetailView):
    model=Note 
    template_name='dashboard/partials/note_detail.html'
    context_object_name = 'note'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Note.active_notes.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the form pre-populated with the note instance
        context['form'] = NoteForm(instance=self.object)
        return context
    
class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'components/modal.html'  # we’ll reuse the same modal
    login_url = reverse_lazy('login')

    def get_queryset(self):
        # Ensure user can only edit their own notes
        return Note.active_notes.filter(user=self.request.user)

    def get_success_url(self):
        # After editing, return to note detail page or list
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ensure the note object is available in context
        context['note'] = self.object
        return context


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('list')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Note.active_notes.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Soft delete instead of actual deletion
        self.object.is_deleted = True
        self.object.save()
        return redirect(self.success_url)