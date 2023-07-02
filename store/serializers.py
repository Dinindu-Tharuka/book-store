from rest_framework import serializers
from .models import BookStore, Book



class BookSerializer(serializers.ModelSerializer):
    store_id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year', 'store_id']

    def create(self, validated_data):
        bookstore_id = self.context['bookstore_id']
        return Book.objects.create(store_id=bookstore_id, **validated_data)

class StoreSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = BookStore
        fields = ['id', 'user_id']

    def create(self, validated_data):
        user_id = self.context['user_id']
        return BookStore.objects.create(user_id=user_id, **validated_data)