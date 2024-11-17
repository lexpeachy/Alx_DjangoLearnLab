from django.shortcuts import render

from django.shortcuts import render
from .models import Book, ExampleForm

def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'book_list.html', {'books': books})

from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

