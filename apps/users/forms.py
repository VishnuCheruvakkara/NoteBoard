from django import forms
from django.contrib.auth.forms import UserCreationForm 
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
            field.widget.attrs['class']='form-control'