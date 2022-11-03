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

        fields = ('id', 'name', 'thumbnail', 'description', 'studio_images', 'phone', 'naver_link','instagram_link','open_time', 'close_time', 'address', 'town', 'follow_users')




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

class ReviewSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'author', 'content', 'studio', 'rating', 'created_at')