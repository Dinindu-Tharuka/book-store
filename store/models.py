from django.db import models
from django.conf import settings
from uuid import uuid4

    

class BookStore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.DateField(null=True)
    store = models.ForeignKey(BookStore, on_delete=models.CASCADE, related_name='books')


