from django.db import models
from django.conf import settings
from movies.models import Movie


class TastingTag(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return self.name


class Tastingroom(models.Model):
    movie = models.ForeignKey(Movie, null=False, on_delete=models.CASCADE, related_name='movie_tastingrooms')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='author_tastingrooms')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participating_tastingrooms')
    tags = models.ManyToManyField(TastingTag, related_name='tags_tastingrooms', blank=True)
    title = models.CharField(max_length=255, null=False)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.title


'''
class Talk(models.Model):
    tastingroom = models.ForeignKey(Tastingroom, null=False, on_delete=models.CASCADE, related_name='talks')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='talks')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
'''