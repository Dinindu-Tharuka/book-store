from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from . import views 


urlpatterns = [    
    path('login/', views.login_view, name='login'),
    path('books/', views.get_books, name='book_details'),
    path('books/add/', views.add_to_books, name='add_to_books'),
    path('books/update/', views.update_book, name='update_book'),
    path('register/', views.register, name='register'),
    path('books/delete/', views.delete_book, name='delete')
]