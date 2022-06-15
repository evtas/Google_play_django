from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    star_rating = models.FloatField()
    download_times = models.CharField(max_length=20)
    content_rating = models.CharField(max_length=20)
    introduction = models.TextField()
    update_time = models.DateField()
    image = models.URLField()
    url = models.URLField()
    apk = models.FilePathField()

    def __str__(self):
        return "%s" % self.name


class GamesGenre(models.Model):
    name = models.ForeignKey(Games, on_delete=models.CASCADE)
    genre = models.CharField(max_length=20)
