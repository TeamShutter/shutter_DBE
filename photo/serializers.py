from dataclasses import fields
from rest_framework import serializers
from studio.serializers import StudioSerializer
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    studio = StudioSerializer(read_only=True)
    class Meta:
        model = Photo
        fields = "__all__"

# class PhotoByStudioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Photo
#         fields = ('id', 'sex', 'photoUrl', 'studio', 'tags' 'like_users')


# class AllPhotoSerializer(serializers.Serializer):
#     class Meta:
#         model=Photo
#         fields = ('id', 'photo_url')