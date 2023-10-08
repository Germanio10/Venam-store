from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from .models import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-grp'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-grp'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-grp'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-grp'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-grp'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-grp'
    }))
    
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2')
        

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-grp'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-grp'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-grp'
    }))
    
    class Meta:
        model = User
        fields = ('email', 'password')
    