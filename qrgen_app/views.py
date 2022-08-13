
from django.shortcuts import render
from .forms import *
# Create your views here.

def index(request):
    form = QrGenForm()
    context = {'form':form}
    return render (request, 'qrgen/index.html', context)

def result(request):
    if request.method == 'POST':
        user_link = request.POST['link']
        user_qr_name = request.POST['qr_name']
        user_color = request.POST['color'].replace('#', '')
        print(user_color)
        api_url = f'http://api.qrserver.com/v1/create-qr-code/?data={user_link}&size=100x100&color={user_color}'
        context = {'imgsrc':api_url, 'qrname': user_qr_name}
    return render (request, 'qrgen/result.html', context)