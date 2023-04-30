
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import User
from django.forms import ModelForm

class RegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    password2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    is_fudhotel=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'hidden'}))

class Meta(UserCreationForm.Meta):
        model= User
        fields={'username', 'password1', 'password2','is_fudhotel'}


    
