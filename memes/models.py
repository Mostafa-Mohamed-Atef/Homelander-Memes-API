from django.db import models

# Create your models here.
class Memes(models.Model):
    def __str__(self) -> str:
        return self.name
    image = models.ImageField(upload_to='memes/files/images/',blank=True, null=True)
    name = models.CharField(max_length=225)
    season = models.PositiveSmallIntegerField(null=True, blank=True)
    episode = models.PositiveSmallIntegerField(null=True, blank=True)
    tags = models.CharField(max_length=225,null=True, blank=True)
    video = models.CharField(max_length=225,null=True, blank=True)
    # video = models.FileField(upload_to='memes/files/images/',null=True, blank=True)

    #to know which user added this 
    # user = models.ForeignKey()