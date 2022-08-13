from . import views
from django.urls import path, include

app_name = 'qruser'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.signup, name='logout'),
    
]