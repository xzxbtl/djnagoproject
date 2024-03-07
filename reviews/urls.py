from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('reviews/', views.index, name="reviews"),
    path('reviews/create/', views.create, name="reviewscreate"),
    path('<str:username>/<int:id>/', views.review_cart, name='reviewcart')
]