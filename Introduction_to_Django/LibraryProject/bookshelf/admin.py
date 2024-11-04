from django.contrib import admin
from .models import Book
# Register your models here.

class Bookadmin(admin.ModelAdmin):
    list_filter = ("title", "author", "publication_year")
    search_fields =()


admin.site.register(Book,Bookadmin)