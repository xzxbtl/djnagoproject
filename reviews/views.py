from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .forms import UserCreateNote
from .models import Reviews


def index(request):
    page = request.GET.get('page', 1)
    user = request.user
    reviews = Reviews.objects.all()  # Исправьте notes на reviews
    paginator = Paginator(reviews, 3)
    current_page = paginator.page(int(page))
    context = {
        'reviews': current_page,  # Исправьте notes на reviews
        'user': user
    }
    return render(request, 'reviews.html', context=context)


def create(request):
    if request.method == "POST":
        reviews = UserCreateNote(request.POST)
        if reviews.is_valid():
            new_note = Reviews()
            new_note.user = request.user
            new_note.description = reviews.cleaned_data['description']
            new_note.save()
    else:
        reviews = UserCreateNote()

    return render(request, 'reviews-create.html', {'form': reviews})


def review_cart(request, username, id):
    reviews_cart = get_object_or_404(Reviews, id=id)
    context = {
        'reviews': reviews_cart,
    }
    return render(request, 'cart-review.html', context=context)

