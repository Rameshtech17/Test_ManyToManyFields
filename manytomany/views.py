from django.shortcuts import render
from .models import Book, Author, Album, Track, Class, Student
from .serializers import BookSerializer, AuthorSerializer, AlbumSerializer, TrackSerializer, AlbumTrackSerializer, \
    StudentSerilizer, ClassSerializer, ClassStudentSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.


class BookView(APIView):

    def get(self, request):
        school_qury = Book.objects.all()
        serializer = BookSerializer(school_qury, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AutherView(APIView):

    def get(self, request):
        school_qury = Author.objects.all()
        serializer = AuthorSerializer(school_qury, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumView(APIView):

    def get(self, request):
        school_qury = Album.objects.all()
        serializer = AlbumSerializer(school_qury, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrackView(APIView):

    def get(self, request):
        school_qury = Track.objects.all()
        serializer = TrackSerializer(school_qury, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrackSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumTrackView(APIView):

    def get(self, request):
        school_qury = Album.objects.all()
        serializer = AlbumTrackSerializer(school_qury, many=True)
        return Response(serializer.data)


class ClassView(APIView):

    def get(self, request):
        school_qury = Class.objects.all()
        serializer = ClassSerializer(school_qury, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentView(APIView):

    def get(self, request):
        school_qury = Student.objects.all()
        serializer = StudentSerilizer(school_qury, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerilizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassStudentView(APIView):

    def get(self, request):
        school_qury = Class.objects.all()
        serializer = ClassStudentSerializer(school_qury, many=True)
        return Response(serializer.data)
