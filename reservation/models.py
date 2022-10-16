from django.utils import timezone
from django.db import models
from account.models import User

from studio.models import AssginedTime, Studio

# Create your models here.
class Reservation(models.Model):
    STATE_CHOICES = ((1, 'not_confirmed'),(2,'confirmed'),(3,'canceled'))

    user = models.ForeignKey(User, null= True, blank=True, on_delete=models.CASCADE)
    assigned_time = models.ForeignKey(AssginedTime, null = True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=150, default='reservation_description')
    state = models.IntegerField(choices=STATE_CHOICES, default = 1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return(f"{self.user.username}'s reservation : {self.id}")

    def state_change(self, state):
        if state == 'confirmed':
            self.state = 2
        elif state == 'unconfirmed':
            self.state = 1
        elif state == 'canceled':
            self.state = 3
        self.save()
    