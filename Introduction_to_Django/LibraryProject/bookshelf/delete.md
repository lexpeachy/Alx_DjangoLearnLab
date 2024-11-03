
#### Delete Operation

```python
# Delete the book instance
book.delete()

# Confirm deletion by trying to retrieve all books
books = Book.objects.all()
print(books)  # Expected output: <QuerySet []> (indicating no books exist)
