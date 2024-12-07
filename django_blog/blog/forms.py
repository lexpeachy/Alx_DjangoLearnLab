from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from .models import Post
from taggit.forms import TagWidget

from django import forms
import autocomplete_light
from autocomplete_light.contrib import taggit_tagfield
from models import MyModel

class MyModelForm(forms.ModelForm):
    tags = taggit_tagfield.TagField(widget=taggit_tagfield.TagWidget('TagAutocomplete'))
    class Meta:
        model = MyModel
        widgets = {
            'tags': autocomplete_light.TextWidget('TagAutocomplete'),
        }


from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']