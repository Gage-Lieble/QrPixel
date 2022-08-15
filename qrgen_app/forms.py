from tkinter.ttk import Label
from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.widgets import TextInput

class QrGenForm(forms.ModelForm):
    class Meta:
        model = QrGenModel
        fields = '__all__'
        exclude = ['owner']
        labels = {
            'qr_name': 'Name Your Code',
            'link': 'Your Link'
        }
        widgets ={
            'qr_name': TextInput(attrs={'autocomplete':'off'}),
            'link': TextInput(attrs={'autocomplete':'off'}),
            'color': TextInput(attrs={'type':'color'}),

            }