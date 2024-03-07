from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import UserCreateNote
from .models import Notes, Category
from django.shortcuts import get_object_or_404


def index(request):
    page = request.GET.get('page', 1)
    user = request.user
    notes = Notes.objects.filter(category__name="open")
    paginator = Paginator(notes, 6)
    current_page = paginator.page(int(page))
    context = {
        'notes': current_page,
        'user': user
    }
    return render(request, 'to-do.html', context=context)


def create(request):
    if request.method == "POST":
        note_form = UserCreateNote(request.POST)
        if note_form.is_valid():
            privacy = request.POST.get('privacy')
            new_note = Notes()  # Создаем новый объект Notes
            new_note.user = request.user
            new_note.description = note_form.cleaned_data['description']

            category = None
            if privacy == 'private':
                category = Category.objects.get(name='private')
            elif privacy == 'open':
                category = Category.objects.get(name='open')

            new_note.category = category
            new_note.save()  # Сохраняем новую запись в базе данных
    else:
        note_form = UserCreateNote()

    return render(request, 'to-do-create.html', {'form': note_form})


def note(request, username, id):
    note_cart = get_object_or_404(Notes, id=id)
    context = {
        'note': note_cart
    }
    return render(request, 'cart-to-do.html', context=context)


def private_notes(request, username):
    page = request.GET.get('page', 1)
    user = request.user
    notes = Notes.objects.filter(user=user, category__name="private")  # Фильтрация заметок по пользователю
    paginator = Paginator(notes, 6)
    current_page = paginator.page(int(page))
    context = {
        'notes': current_page,
        'user': user
    }
    return render(request, 'to-do.html', context=context)