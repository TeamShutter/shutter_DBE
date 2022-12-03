from email.policy import default
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
from django.contrib.auth.models import AbstractUser	# AbstractUser 불러오기

class User(AbstractUser):
    SEX = (('male', 'male'), ('female', 'female'))

    last_name = None
    first_name = None
    name = models.CharField(max_length=10, default='name')
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length = 20, choices = SEX, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return(f'{self.email}')

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def phone_update(self, phone_number):
        self.phone = phone_number
        self.save()
        return 
