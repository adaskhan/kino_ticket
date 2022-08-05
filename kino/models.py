from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from datetime import date


class Film(models.Model):
    name = models.CharField(max_length=400)
    img = models.ImageField()
    raiting = models.FloatField()
    genre = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()
    trailer = EmbedVideoField()

    def __str__(self) -> str:
        return self.name


class Session(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    kino_teatre = models.CharField(max_length=200)
    tic_price = models.IntegerField()

    @property
    def is_past_due(self):
        return date.today() < self.start_time


class News(models.Model):
    img = models.ImageField()
    date = models.DateField()
    title = models.CharField(max_length=600)
    text = models.TextField()


class History(models.Model):
    date = models.DateTimeField()
    owner = ForeignKey(User, on_delete=CASCADE)
    ticket = ForeignKey(Session, on_delete=CASCADE)

    @property
    def is_past_due(self):
        return date.today() > self.date


class Review(models.Model):
    author = ForeignKey(User, on_delete=CASCADE)
    text = models.TextField()
    film = ForeignKey(Film, on_delete=CASCADE)


