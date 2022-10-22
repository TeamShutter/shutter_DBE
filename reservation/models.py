from django.utils import timezone
from django.db import models
from account.models import User

from studio.models import AssignedTime, Studio

# Create your models here.
class Reservation(models.Model):
<<<<<<< HEAD
    STATE_CHOICES = ((1, 'unconfirmed'),(2,'confirmed'),(3,'canceled'))
=======
    STATE_CHOICES = ((1, 'not_confirmed'),(2,'confirmed'),(3,'canceled'), (4, 'done'))
>>>>>>> 4e604bf7c70cc85757e8b27af508479639b7b6ab

    user = models.ForeignKey(User, null= True, blank=True, on_delete=models.CASCADE)
    assigned_time = models.ForeignKey(AssignedTime, null = True, blank=True, on_delete=models.CASCADE)
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
        elif state == 'done':
            self.state = 4
        self.save()
    