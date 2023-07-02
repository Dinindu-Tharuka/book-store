from django.contrib import admin
from .models import Book, BookStore

@admin.register(BookStore)
class BookStoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publication_year', 'store']