from django import forms
from django.forms import ModelForm
from .models import *

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'autocomplete':'off'}))
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', max_length=10,)
    

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'autocomplete':'off'}))
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', max_length=10,)