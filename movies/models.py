from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, default="")
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    image = models.CharField(max_length=105)
    description = models.CharField(max_length=1200)
    genre = models.CharField(max_length=255)
    rating = models.FloatField()

    class Meta:
        ordering = ["rating"]

    def __str__(self):
        return self.title