from django.contrib import admin
from .models import Book, Author, Album, Track, Class, Student

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Class)
admin.site.register(Student)
