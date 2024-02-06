from rest_framework import serializers
from .models import Book, Author, Language


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=True)

    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False)

    class Meta:
        model = Book
        fields = "__all__"
