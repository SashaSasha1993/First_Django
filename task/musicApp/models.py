from django.db import models

# Create your models here.
class Genre (models.Model):
    genre_index = models.IntegerField(primary_key = True)
    genre_type = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_type

class Artist (models.Model):
    name = models.CharField(max_length= 100)
    genre = models.ForeignKey(Genre)
    country = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
class Song (models.Model):
    song_name = models.CharField(max_length = 100)
    artist = models.ForeignKey(Artist)
    def __str__(self):
        return self.song_name

