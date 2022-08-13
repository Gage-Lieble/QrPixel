from django import forms
from django.forms import ModelForm
from .models import *

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': ' Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ' Password'}), label='Password', max_length=10,)
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': ' Email'}))

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': ' Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ' Password'}), label='Password', max_length=10,)