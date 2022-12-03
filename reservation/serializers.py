from dataclasses import fields
from rest_framework import serializers

from .models import Reservation
from studio.serializers import AssignedTimeSerializer, ProductSerializer
class ReservationSerializer(serializers.ModelSerializer):
    assigned_time = AssignedTimeSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = "__all__"

