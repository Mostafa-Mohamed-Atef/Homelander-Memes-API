from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Memes(models.Model):
    def __str__(self) -> str:
        return self.name
    type_choises = (('image', 'image'),('video', 'video'), ('gif', 'gif'), ('all', 'all'))
    name = models.CharField(max_length=225)
    type = models.CharField(max_length=225, choices=type_choises, blank=True, null=True)
    image = models.ImageField(upload_to='memes/files/images/',blank=True, null=True)
    video = models.FileField(upload_to='memes/files/images/',null=True, blank=True)
    video_link = models.CharField(max_length=225,null=True, blank=True)
    season = models.PositiveSmallIntegerField(null=True, blank=True)
    episode = models.PositiveSmallIntegerField(null=True, blank=True)
    tags = models.CharField(max_length=225,null=True, blank=True)

    #to know which user added this 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memes', null=True, blank=True)