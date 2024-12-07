from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import UserAttributeSimilarityValidator

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']