from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name="todomain"),
    path('create/', views.create, name="createtodo"),
    path('<str:username>/<int:id>/', views.note, name='notecart'),
    path('<str:username>/private/', views.private_notes, name='notecartprivate')
]