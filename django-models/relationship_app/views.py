from django.shortcuts import render
from .models import Book

def list_books(request):
    books=Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from .forms import BookForm
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Library  # Adjust the model import as needed
from django.contrib.auth.forms import UserCreationForm

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth import login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to a home page or dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'logout.html')


["from django.contrib.auth import login", "from django.contrib.auth.forms import UserCreationForm"]