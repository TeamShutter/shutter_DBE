from django.db import models
from photo.models import Photo

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ManyToManyField(Photo, through='Photo_Tag')

    def __str__(self):
        return(f"{self.name}")

class Photo_Tag(models.Model):
    photo = models.ForeignKey(Photo, null=True, blank=True, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.photo}_{self.tag}")