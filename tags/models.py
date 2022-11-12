from django.db import models
from photo.models import Photo

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)
    photos = models.ManyToManyField(Photo, blank=True ,through='PhotoTag', related_name='tags')

    def __str__(self):
        return(f"{self.name}")

class PhotoTag(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.photo}_{self.tag}")