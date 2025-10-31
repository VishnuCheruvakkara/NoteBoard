from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from users.models import CustomUser

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=CustomUser 
        fields=['username','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #Add Bootstrap classes 
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control nb-input',
            })

        # Add placeholders for better UX
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control nb-input',
            'placeholder': 'Enter your email or username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control nb-input',
            'placeholder': 'Enter your password'
        })
    )