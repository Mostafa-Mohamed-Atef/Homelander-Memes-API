from django.db import models
# Create your models here.
class MovieData(models.Model):
    
    name = models.CharField(max_length=225)
    duration = models.FloatField()
    rating = models.FloatField()

    def __str__(self) -> str:
        return self.name