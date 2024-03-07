from django import forms
from .models import Reviews
from users.models import User


class UserCreateNote(forms.Form):
    class Meta:
        model = Reviews
        fields = ("username", "description")

    description = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Input your notes",
            }
        )
    )
