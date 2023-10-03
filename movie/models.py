from django.db import models


# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Director(models.Model):
    director_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Cast(models.Model):
    cast_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    year_released = models.IntegerField()
    duration = models.IntegerField()
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    cast = models.ManyToManyField(Cast)
    # The project assumes that a movie can only have one director
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
