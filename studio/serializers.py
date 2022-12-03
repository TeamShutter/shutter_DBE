from rest_framework import serializers
from .models import AssignedTime, Photographer, Place, Review, Studio, Product, OpenedTime, StudioImage

#  description = models.TextField(default='description')
    
#     phone = models.CharField(max_length=50, default='010-0000-0000')
#     openTime = models.CharField(max_length=50, default='openTime')
#     closeTime = models.CharField(max_length=50, default='closeTime')
#     follow_users = models.ManyToManyField(User, blank=True, related_name= 'studio_follows', through ='Follow') 
#     address = models.CharField(max_length=50, default='address')
#     town = models.CharField(max_length=50, default='town')
#     photoshop = models.IntegerField(choices=PHOTOSHOP_CHOICES, default=0)
#     thumbnail = models.CharField(max_length=500, default="url")

class StudioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudioImage
        fields = ('id', 'url')
class StudioSerializer(serializers.ModelSerializer):
    studio_images = StudioImageSerializer(many=True)

    class Meta:
        model = Studio

        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class PlaceSerializer(serializers.Serializer):

    class Meta:
        model = Place
        fileds = ('studio', 'name', 'description', 'address')
    

class OpenedTimeSerializer(serializers.ModelSerializer):
    # studio = StudioSerializer(many=True)

    class Meta:
        model = OpenedTime
        fields = "__all__"

class PhotographerSerializer(serializers.ModelSerializer):
    # studio = StudioSerializer()

    class Meta:
        model = Photographer
        fields = "__all__"

class AssignedTimeSerializer(serializers.ModelSerializer):
    photographer = PhotographerSerializer(read_only=True)
    opened_time = OpenedTimeSerializer(read_only=True)
    # is_absence = serializers.BooleanField(default=False)

    class Meta:
        model = AssignedTime
        fields = "__all__"
class ReviewSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'author', 'content', 'studio', 'rating', 'created_at')