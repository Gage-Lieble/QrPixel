from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.widgets import TextInput

class QrGenForm(forms.ModelForm):
    class Meta:
        model = QrGenModel
        fields = '__all__'
        exclude = ['owner']
        widgets ={'color': TextInput(attrs={'type':'color'})}