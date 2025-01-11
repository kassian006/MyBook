from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Author(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class Genre(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class Book(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookLanguages(serializers.ModelSerializer):
    class Meta:
        model = BookLanguages
        fields = '__all__'


class Rating(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class Favorite(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteBook(serializers.ModelSerializer):
    class Mata:
        model = FavoriteBook
        fields = '__all__'


class Quote(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'