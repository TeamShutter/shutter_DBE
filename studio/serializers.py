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
<<<<<<< HEAD
        fields = ('id', 'name', 'thumbnail', 'description', 'studio_images', 'phone', 'naver_link','instagram_link','open_time', 'close_time', 'address', 'town', 'follow_users')


class ProductSerializer(serializers.ModelSerializer):
    # studio = StudioSerializer(read_only=True) #이거 없으니까 product serializer 에서 studio data가 안보였음
=======

        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):
>>>>>>> ffb224775071ee86ac212eb1d2c53c0ce0d9ba9c

    class Meta:
        model = Product
        fields = "__all__"

class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = ('studio', 'name', 'description', 'address')
    

class OpenedTimeSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    # studio = StudioSerializer(many=True)
=======
    studio = StudioSerializer(read_only=True)
>>>>>>> ffb224775071ee86ac212eb1d2c53c0ce0d9ba9c

    class Meta:
        model = OpenedTime
        fields = "__all__"

class PhotographerSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    # studio = StudioSerializer(many=True)
=======
    # studio = StudioSerializer()
>>>>>>> ffb224775071ee86ac212eb1d2c53c0ce0d9ba9c

    class Meta:
        model = Photographer
        fields = "__all__"
<<<<<<< HEAD
=======

>>>>>>> ffb224775071ee86ac212eb1d2c53c0ce0d9ba9c
class AssignedTimeSerializer(serializers.ModelSerializer):
    photographer = PhotographerSerializer(read_only=True)
    opened_time = OpenedTimeSerializer(read_only=True)
    # is_absence = serializers.BooleanField(default=False)

    class Meta:
        model = AssignedTime
        fields = "__all__"
<<<<<<< HEAD

=======
>>>>>>> ffb224775071ee86ac212eb1d2c53c0ce0d9ba9c
class ReviewSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'author', 'content', 'studio', 'rating', 'created_at')