from rest_framework import serializers
from .models import AssignedTime, Photographer, Place, Studio, Product, OpenedTime

#  description = models.TextField(default='description')
    
#     phone = models.CharField(max_length=50, default='010-0000-0000')
#     openTime = models.CharField(max_length=50, default='openTime')
#     closeTime = models.CharField(max_length=50, default='closeTime')
#     follow_users = models.ManyToManyField(User, blank=True, related_name= 'studio_follows', through ='Follow') 
#     address = models.CharField(max_length=50, default='address')
#     town = models.CharField(max_length=50, default='town')
#     photoshop = models.IntegerField(choices=PHOTOSHOP_CHOICES, default=0)
#     thumbnail = models.CharField(max_length=500, default="url")
class StudioSerializer(serializers.Serializer):
    name = serializers.CharField()
    class Meta:
        model = Studio
        fields = ('name', 'phone', 'open_time', 'close_time', 'address', 'town', 'follow_users', 'thumbnail')

class ProductSerializer(serializers.Serializer):
    # studio = StudioSerializer(read_only=True)  이거 들어가면 안되는데 왜 그런거지??..

    class Meta:
        model = Product
        fields = ('studio', 'name', 'description', 'price', 'duration', 'created_at', 'updated_at')

class PlaceSerializer(serializers.Serializer):

    class Meta:
        model = Place
        fileds = ('studio', 'name', 'description', 'address')
    

class OpenedTimeSerializer(serializers.Serializer):
    # studio = StudioSerializer(many=True)

    class Meta:
        model = OpenedTime
        fields = ('studio', 'date', 'hour', 'minute')

class PhotographerSerializer(serializers.Serializer):
    # studio = StudioSerializer(many=True)

    class Meta:
        model = Photographer
        fields = ('studio', 'name')

class AssignedTimeSerializer(serializers.Serializer):
    # photographer = PhotographerSerializer(many=True) 이부분 어떡하지??..
    # openedTime = OpenedTimeSerializer(many=True)
    # is_absence = serializers.BooleanField(default=False)

    class Meta:
        model = AssignedTime
        fields = ('studio', 'product', 'is_absence')

