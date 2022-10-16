from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser	# AbstractUser 불러오기

class User(AbstractUser):
    last_name = None
    first_name = None

    def __str__(self):
        return(f'{self.id}')

