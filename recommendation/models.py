from django.db import models

from user.models import User
from movie.models import Movie


# Create your models here.
class Recommendation(models.Model):
    recommendation_id = models.IntegerField(primary_key=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)

