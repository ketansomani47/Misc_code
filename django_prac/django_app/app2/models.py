from django.db import models

# Create your models here.
class Movie(models.Model):
    class Meta:
        db_table = "movie"
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Review(models.Model):
    class Meta:
        db_table = "review"
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, related_name='review')
    comment = models.TextField()

