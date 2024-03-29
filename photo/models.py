from django.db import models
from accounts.models import User
from django.utils import timezone
from studio.models import Studio

# Create your models here.
class Photo(models.Model):
    SEX = (('male', 'male'), ('female', 'female'))
    TYPE = ((1, '프로필 사진'),(2,'중명 사진'),(3,'단체 사진'), (4, '컨셉 사진'))
    COLOR = ((1, "white"),(2, "gray"),(3, "black"),(4, "pink"),(5, "red"),(6, "wheat"),(7, "orange"),(8, "yellow"),(9, "greenyellow"),(10, "olive"),(11, "skyblue"),(12, "navy"),(13, "saddlebrown"),(14, "purple"))
    sex = models.CharField(max_length = 20, choices = SEX)
    # category = models.CharField(max_length=50, default='category')
    photo_url = models.CharField(max_length=500, default="url")
    studio = models.ForeignKey(Studio, null = True, on_delete=models.CASCADE)
    #address 는 외래키, 태그는 다대다(하나의 사진에서 여러개의 태그를 등록할ㅇ 수 있도록)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_photos', through='Like')
    price = models.IntegerField(blank=True, null=True, default=0)
    color = models.IntegerField(choices=COLOR, blank=True, null=True, default=1)
    type = models.IntegerField(choices=TYPE, blank=True, null=True, default=1)
    def __str__(self):
        return(f"{self.studio.name}'s photo_{self.id}")

    class Meta:
        db_table = "photo"

# 사진에서 줘야하는 정보 : 성별, 사진, 사진이 속한 스튜디오, 사진의 태그, 좋아요를 누른 사람들

class Like(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return(f"{self.user.username}'s like for photo_{self.photo.id}")

    class Meta:
        db_table = 'like'




