from django.shortcuts import render
from rest_framework.views import APIView
from photo.models import Photo
from .models import Tag, PhotoTag
from .serializers import TagSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class AllTagView(APIView):
    def get(self, request):
        try:
            tag = Tag.objects.all()
            serializer = TagSerializer(tag, many=True)
            return Response({"data" : serializer.data, "success": "get all tags"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "failed to get all tags"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:

            tag_name = request.data.get('name')

            try:
                Tag.objects.create(name=tag_name)
            except:
                Response({"1":"1"})
            return Response({"success": "tag created"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "failed to create tag"}, status=status.HTTP_400_BAD_REQUEST)

class TagView(APIView):
    def get(self, request, tag_id):
        tag = Tag.objects.get(id=tag_id)
        serializer = TagSerializer(tag)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

class PhotoTagView(APIView):
    def post(self, request):
        tag_name = request.data.get('tag_name')
        try:
            photo_id_str = request.data.get('photo_id_str')
            photo_id_list = photo_id_str.split(' ')
        
            tag = Tag.objects.get(name=tag_name)
        
            for photo_id in photo_id_list:
                photo = Photo.objects.get(id=int(photo_id))
                PhotoTag.objects.create(photo=photo, tag=tag)
        except:
            return Response({"1":"1"})
        return Response({"success": "photo tag objects created"}, status=status.HTTP_200_OK)