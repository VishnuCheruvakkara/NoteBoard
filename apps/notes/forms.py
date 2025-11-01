from django import forms 
from .models import Note 

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control nb-input',
                'placeholder': 'Enter title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control nb-input',
                'placeholder': 'Write your note...'
            }),
        }