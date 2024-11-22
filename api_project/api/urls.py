from django import path
from .views import BookListCreateAPIView

urlpatterns = [
    path("api.urls/books", views.BookListCreateAPIView.as_view(), name="book_list_create"),
]