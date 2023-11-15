from django.db import models

class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    genre = models.CharField(max_length=255)
    rating = models.FloatField()

    class Meta:
        ordering = ["rating"]

    def __str__(self):
        return self.title