
from . import views
from django.urls import path
app_name = 'main'

urlpatterns=[
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
]
