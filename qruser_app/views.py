
from django.shortcuts import render
from qrgen_app.models import *
from qrgen_app.forms import QrGenForm
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
            ##### THIS ISNT WORKING VVVV
            new_user = authenticate(username=su_form.cleaned_data['username'], password=su_form.cleaned_data['password'])
            login(request, new_user)
        return HttpResponseRedirect(reverse('qruser:profile'))

def userlogin(request):
    if request.method == 'GET':
        li_form = LoginForm()
        context = {'form':li_form}
        return render(request, 'qruser/login.html', context)
    elif request.method == 'POST':
        li_form = LoginForm(request.POST)
        if li_form.is_valid():
            password = li_form.cleaned_data['password']
            user = authenticate(request, username=li_form.cleaned_data['username'], password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('qruser:profile'))
            else:
                # Checks if user exists
                li_form.add_error('username', 'Invalid username or password')
                return render(request, 'qruser/login.html', {'form': li_form})

def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('qruser:login'))

def profile(request):
    saved_qr = QrGenModel.objects.all().filter(owner=request.user)
    
    context = {'usercodes':saved_qr}
    return render (request, 'qruser/profile.html', context)

def saveQr(request, qrname, qrlink, qrcolor):
    model = QrGenModel(owner=request.user, link=qrlink.replace('`', '/'), qr_name=qrname, color=qrcolor)
    model.save()
    return HttpResponseRedirect(reverse('qruser:profile'))

def deleteQr(request, qrname):
    if QrGenModel.objects.filter(qr_name=qrname).exists():
        qrcode = QrGenModel.objects.get(qr_name=qrname)
        qrcode.delete()
    return HttpResponseRedirect(reverse('qruser:profile'))