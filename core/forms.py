from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Tweet


class SignUpForm(UserCreationForm):
    display_name = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "display_name", "email", "password1", "password2")


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(
                attrs={"placeholder": "What's on your mind?", "label": "", "rows": 4}
            )
        }
