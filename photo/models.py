from django.db import models
from accounts.models import User
from django.utils import timezone
from studio.models import Studio


# Create your models here.
class Photo(models.Model):
    SEX = (('male', 'male'), ('female', 'female'))

    sex = models.CharField(max_length = 20, choices = SEX)
    # category = models.CharField(max_length=50, default='category')
    photo_url = models.CharField(max_length=500, default="url")
    studio = models.ForeignKey(Studio, null = True, on_delete=models.CASCADE)
    #address 는 외래키, 태그는 다대다(하나의 사진에서 여러개의 태그를 등록할 수 있도록)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_photos', through='Like')
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "photo"

# 사진에서 줘야하는 정보 : 성별, 사진, 사진이 속한 스튜디오, 사진의 태그, 좋아요를 누른 사람들

class Like(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'like'