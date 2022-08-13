
from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def signup(request):

    if request.method == 'GET':
        su_form = SignUpForm()
        context = {'form':su_form}
        return render (request, 'qruser/signup.html', context)
    elif request.method == 'POST':
        su_form = SignUpForm(request.POST)
        if su_form.is_valid():
            user = User.objects.create_user(
                username = su_form.cleaned_data['username'],
                password = su_form.cleaned_data['password'],
                email = su_form.cleaned_data['email'],
            )
            # context = {'username': user.username}
        return render (request, 'qruser/profile.html')

def login(request):
    if request.method == 'GET':
        li_form = LoginForm()
        context = {'form':li_form}
        return render (request, 'qruser/login.html', context)
    elif request.method == 'POST':
        li_form = LoginForm(request.POST)
        if li_form.is_valid():
            password = li_form.cleaned_data['password']
            user = authenticate(request, username=li_form.cleaned_data['username'], password=password)
            if user is not None:
                login(request, user)
                return render (request, 'qruser/profile.html')
            

def profile(request):
    return render (request, 'qruser/profile.html')