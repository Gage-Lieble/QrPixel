
from dis import Instruction
from django.urls import path, include
from . import views

app_name = 'genapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('coderesult/', views.result, name='result'),
    path('instructions/', views.instructions, name='instructions')
]
