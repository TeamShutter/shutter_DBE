from email.policy import default
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
from django.contrib.auth.models import AbstractUser	# AbstractUser 불러오기

class User(AbstractUser):
    last_name = None
    first_name = None
    name = models.CharField(max_length=10, default='name')


    def __str__(self):
        return(f'{self.name}')

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
