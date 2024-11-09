from relationship_app import Author, Book

author=Author.objects.get(name="Author name")
books_by_author= Book.objects.filter(author=author)
for book in books_by_author:
    print (book.title)

from relationship_app.models import Library

library = Library.objects.get(name="Library Name")
books_in_library = library.books.all()
for book in books_in_library:
    print(book.title)

from relationship_app.models import Library, Librarian

library = Library.objects.get(name="Library Name")
librarian = Librarian.objects.get(library=library)
print(librarian.name)
