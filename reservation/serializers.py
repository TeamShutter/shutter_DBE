from dataclasses import fields
from rest_framework import serializers

from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('user', 'assigned_time', 'description', 'state', 'created_at')

