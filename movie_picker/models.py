from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    overview = models.TextField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=5, decimal_places=1)
    image = models.TextField()
    def __str__(self): return f'{self.title} ({self.release_date})'