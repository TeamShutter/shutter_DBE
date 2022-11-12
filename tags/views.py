from django.shortcuts import render
from rest_framework.views import APIView
from .models import Tag
from .serializers import TagSerializer
from rest_framework.response import Response
from rest_framework import status
from photo.models import Photo


# Create your views here.
class AllTagView(APIView):
    def get(self, request):
        try:
            tag = Tag.objects.all()
            if request.GET.get('photoId') and request.GET.get('photoId') != '0':
                photo = Photo.objects.filter(id=request.GET.get('photoId'))
                # get을 쓰면 한개로 인식해서 __in 이 안써져서 filter로 설정
                tag = tag.filter(photos__in = photo)
            serializer = TagSerializer(tag, many=True)
            return Response({"data" : serializer.data, "success": "get all tags"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "failed to get all tags"}, status=status.HTTP_400_BAD_REQUEST)
