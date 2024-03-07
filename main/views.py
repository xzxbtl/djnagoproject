from django.shortcuts import render
from todo.models import Notes
from reviews.models import Reviews
from django.http import JsonResponse


def home(request):
    query = request.GET.get('q', None)
    content = {
        'title': 'Home - Main',
    }
    return render(request, 'main/home.html', content)


def about(request):
    content = {
        'title': 'Home - About us',
    }
    return render(request, 'main/about.html', content)







