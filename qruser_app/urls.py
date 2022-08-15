from . import views
from django.urls import path, include

app_name = 'qruser'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.userlogout, name='logout'),
    path('saveqr/<str:qrname>/<str:qrlink>/<str:qrcolor>/', views.saveQr, name='saveqr')

]