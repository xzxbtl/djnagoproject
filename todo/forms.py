from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Notes
from users.models import User
from .models import Category, Notes


class UserCreateNote(forms.Form):
    class Meta:
        model = Notes
        fields = ("username", "name", "description", "category")

    description = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Input your notes",
            }
        )
    )
    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Input NameList"
            }
        )
    )

    privacy = forms.ChoiceField(
        choices=(('private', 'Private'), ('open', 'Open')),
        widget=forms.RadioSelect()
    )



