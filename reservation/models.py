from itertools import product
from django.utils import timezone
from django.db import models
from accounts.models import User

from studio.models import AssignedTime, Place, Product, Studio


# Create your models here.
class Reservation(models.Model):
    STATE_CHOICES = ((1, 'not_confirmed'),(2,'confirmed'),(3,'canceled'), (4, 'done'))
    product = models.ForeignKey(Product, null=True, blank = True, on_delete = models.CASCADE)
    studio = models.ForeignKey(Studio, null = True, blank = True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null= True, blank=True, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE)
    assigned_time = models.ForeignKey(AssignedTime, null = True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=150, default='reservation_description')
    state = models.IntegerField(choices=STATE_CHOICES, default = 1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return(f"{self.user.username}'s reservation : {self.id}")

    # def state_change(self, state):
    #     assigned_id = self.assigned_time
    #     assigned_time = AssignedTime.objects.get(id=assigned_id)
    #     if state == 'confirmed':
    #         self.state = 2
    #         assigned_time.update_absence()
    #     elif state == 'unconfirmed':
    #         self.state = 1
    #         assigned_time.update_absence()
    #     elif state == 'canceled':
    #         self.state = 3
    #         assigned_time.update_absence()
    #     elif state == 'done':
    #         self.state = 4
    #     self.save()
    