from rest_framework import serializers
from .models import Author, Book, Album, Track, Class, Student


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'authors')


class AuthorSerializer(serializers.ModelSerializer):
    book_list = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'last_name', 'book_list')


class AlbumTrackSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'album', 'order', 'title', 'duration']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['album_name', 'artist']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['class_name']


class StudentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']


class ClassStudentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(many=True)

    class Meta:
        model = Class
        fields = ['class_name', 'student']
