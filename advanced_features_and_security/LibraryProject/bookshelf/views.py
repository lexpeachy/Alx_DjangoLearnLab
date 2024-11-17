from django.shortcuts import render

# Create your views here.
#  from django.contrib.auth.decorators import permission_required
# from django.shortcuts import render, get_object_or_404
# from .models import Book

# @permission_required('yourapp.can_view', raise_exception=True)
# def view_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     return render(request, 'book_detail.html', {'book': book})

# @permission_required('yourapp.can_edit', raise_exception=True)
# def edit_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     # Logic to edit the book
#     return render(request, 'edit_book.html', {'book': book})
