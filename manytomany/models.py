from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, default="")
    last_name = models.IntegerField(default=0)

class Book(models.Model):
    authors = models.ManyToManyField(Author, related_name="book_list", blank=True)
    name = models.CharField(max_length=100, default="")
    published = models.BooleanField(default=True)


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order', 'title']
        ordering = ['order']

    def __str__(self):
        return '%d: %d: %s : %d' % (self.id, self.order, self.title, self.duration)

class Class(models.Model):
    class_name = models.CharField(max_length=30)

    def __str__(self):
        return self.class_name

class Student(models.Model):
    std = models.ForeignKey(Class,related_name='student', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        unique_together = ['std', 'first_name', 'last_name']
        ordering = ['first_name']

    def __str__(self):
        return '%d: %s: %s' % (self.id, self.first_name, self.last_name)
