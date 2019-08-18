from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    score = models.FloatField()
    genre = models.CharField(max_length=50)
    editors_choice = models.CharField(max_length=1)

    def __str__(self):
        return self.title
