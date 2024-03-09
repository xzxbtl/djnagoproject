from django.shortcuts import render
from todo.models import Notes
from reviews.models import Reviews
from django.db.models import Q
from django.core.paginator import Paginator


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


def search_page(request):
    query = request.GET.get('q', None)
    page = request.GET.get('page', 1)

    if query is None:
        return render(request, 'main/home.html')

    record_notes = Notes.objects.filter(Q(description__icontains=query) | Q(user__username__icontains=query))[:6]
    record_reviews = Reviews.objects.filter(Q(description__icontains=query) | Q(user__username__icontains=query))[:6]
    search_result = list(record_notes) + list(record_reviews)
    search_input = query

    paginator = Paginator(search_result, 6)
    current_page = paginator.page(int(page))

    content = {
        'search_input': search_input,
        'result': current_page,
        'record_notes': record_notes,
    }
    return render(request, 'main/search.html', content)








