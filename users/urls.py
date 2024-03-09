from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]