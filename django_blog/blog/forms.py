from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from django import forms
from .models import Post
from taggit.forms import TagField  # Import the TagField from django-taggit

class PostForm(forms.ModelForm):
    # Use TagField to enable tagging
    tags = TagField(required=False, help_text="Add comma-separated tags for this post.")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include the 'tags' field



from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']