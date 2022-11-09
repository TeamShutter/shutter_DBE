from datetime import datetime
from email.policy import default
from django.db import models
from django.utils import timezone
from accounts.models import User
# Create your models here.
class Studio(models.Model):
    PHOTOSHOP_CHOICES = ((1, '1'), (2, '2'), (3, '3'))

    name = models.CharField(max_length = 50, default='studio_name')
    description = models.TextField(default='description')
    naver_link = models.CharField(max_length = 200, blank=True, null=True)
    instagram_link = models.CharField(max_length = 200, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    open_time = models.CharField(max_length=50, blank=True, null=True)
    close_time = models.CharField(max_length=50, blank=True, null=True)
    follow_users = models.ManyToManyField(User, blank=True, related_name= 'studio_follows', through ='Follow') 
    address = models.CharField(max_length=50, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    photoshop = models.IntegerField(choices=PHOTOSHOP_CHOICES, default=0)
    thumbnail = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return(self.name)


class Place(models.Model):
    studio = models.ForeignKey(Studio, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='place_name')
    description = models.CharField(max_length=500, default='place_description')
    address = models.CharField(max_length=50, default='address')

    def __str__(self):
        return(self.name)


class Product(models.Model):
    studio = models.ForeignKey(Studio, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='product_name')
    description = models.CharField(max_length=500, default='product_description')
    price = models.IntegerField(default=10000)
    # 상품의 촬영 소요 시간, 기본설정 30분
    duration = models.IntegerField( default=30)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return(self.name)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()


class OpenedTime(models.Model): #이거는 studio랑 manytomany field로 이루어져야할듯??
    studio = models.ForeignKey(Studio, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    hour = models.IntegerField(default=00)
    minute = models.IntegerField(default=00)

    def __str__(self):
        return(f'{self.date}:{self.hour}:{self.minute}') #이러면 곂칠듯 이름? 저장은 되는데 우리가 구분할 필요가 있나?


class Photographer(models.Model):
    studio = models.ForeignKey(Studio, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='photographer_name')

    def __str__(self):
        return(self.name)


# 이부분 수정이 필요할듯.. 애초에 OpenedTime 만들때 photographer를 넣어야하지 않나??
# 이러면 오픈 시간 열고, 또 오픈시간에 사진작가를 저장하는 과정이 필요할듯..
# 그리고 오픈 시간이 선택되면 그 오픈 시간이 스튜디오 다른 사직 작가들은 선택 못해야하는거 아닌가?
class AssignedTime(models.Model): 
    photographer = models.ForeignKey(Photographer, null=True, blank=True, on_delete=models.CASCADE)
    opened_time = models.ForeignKey(OpenedTime, null=True, blank=True, on_delete=models.CASCADE)
    # if photographer is not available, is_absence is True.
    is_available = models.BooleanField(default=False)

    def update_available(self):
        self.is_available = True if self.is_available == False else False
        self.save()

class StudioImage(models.Model):
    url = models.CharField(max_length=500, default='url')
    studio = models.ForeignKey(Studio, null = True, on_delete=models.CASCADE, related_name = "studio_images")



class Review(models.Model):
    RATING_CHOICES = ((1, '1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    content = models.CharField(max_length=200, default='review')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, null=True, blank=True, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES, default =0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "review"


class Follow(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = "follow"