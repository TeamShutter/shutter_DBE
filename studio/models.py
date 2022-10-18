from datetime import datetime
from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.
class Studio(models.Model):
    name = models.CharField(max_length = 50, default='studio_name')

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


class OpenedTime(models.Model):
    studio = models.ForeignKey(Studio, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    hour = models.IntegerField( default=00)
    minute = models.IntegerField( default=00)

    def __str__(self):
        return(f'{self.date}:{self.hour}:{self.minute}')


class Photographer(models.Model):
    studio = models.ForeignKey(Studio, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='photographer_name')

    def __str__(self):
        return(self.name)


class AssginedTime(models.Model):
    photographer = models.ForeignKey(Photographer, null=True, blank=True, on_delete=models.CASCADE)
    opened_time = models.ForeignKey(OpenedTime, null=True, blank=True, on_delete=models.CASCADE)
    # if photographer is not available, is_absence is True.
    is_absence = models.BooleanField(default=False)

