# recommendation/models.py
from django.db import models
from user.models import User
from movie.models import Movie
from django.contrib.auth.models import AbstractUser


class Recommendation(models.Model):
    recommendation_id = models.AutoField(primary_key=True)  # Use AutoField for primary key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s recommendation for {self.movie.title}"


class User(AbstractUser):
    userID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.username

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="recommendation_user_groups",
        related_query_name="recommendation_user_group",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="recommendation_user_permissions",
        related_query_name="recommendation_user_permission",
        blank=True,
        help_text="Specific permissions for this user.",
    )


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MovieYear(models.Model):
    year_id = models.AutoField(primary_key=True)
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class MovieRating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.rating


class Recommendation(models.Model):
    recommendation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s recommendation for {self.movie.title}"
