from django.shortcuts import render

# Create your views here.
def list_books(request):
    books= Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books' : books})

from .forms import BookForm
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Library  

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
