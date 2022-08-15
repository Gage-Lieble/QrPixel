
from django.shortcuts import render
from .forms import *
# Create your views here.

def index(request):
    form = QrGenForm()
    # QrGenForm.owner = request.user


    context = {'form':form}
    return render (request, 'qrgen/index.html', context)

def result(request):
    if request.method == 'POST':
        user_link = request.POST['link']
        user_qr_name = request.POST['qr_name']
        user_color = request.POST['color'].replace('#', '')
        api_url = f'http://api.qrserver.com/v1/create-qr-code/?data={user_link}&size=100x100&color={user_color}'
        context = {'imgsrc':api_url, 'vqrname':str(user_qr_name), 'vqrlink': str(user_link), 'vqrcolor':str(user_color)}
        print(context)
    return render (request, 'qrgen/result.html', context)

