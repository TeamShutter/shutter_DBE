from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.models import User
from studio.models import Studio
from .models import Photo, Like
from .serializers import PhotoSerializer
from studio.serializers import StudioSerializer
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from accounts.authenticate import JWTAuthenticationSafe
# Create your views here.

class AllPhotoView(APIView):
    authentication_classes=[JWTAuthenticationSafe]
    def get(self, request):
        try:
            paginator = PageNumberPagination()
            paginator.page_size = 60
            if request.GET.get('studio_id'):
                studio = Studio.objects.get(id=request.GET.get('studio_id'))
                photo = Photo.objects.filter(studio=studio)
                # serializer = PhotoSerializer(photo, many=True)
            else:
                photo = Photo.objects.all()
                if request.GET.get('town') and request.GET.get('town') != '0':
                    studios = Studio.objects.filter(town = request.GET.get('town'))
                    photo = photo.filter(studio__in = studios)
            result_page = paginator.paginate_queryset(photo, request)
            serializer = PhotoSerializer(result_page, many=True)            
            return Response({"data" : serializer.data, "success": "get all photos"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "failed to get all photos"},status=status.HTTP_400_BAD_REQUEST)

class PhotoView(APIView):
    authentication_classes=[JWTAuthenticationSafe]
    def get(self, request, photo_id):
        try:
            photo = Photo.objects.get(id = photo_id)
            serializer = PhotoSerializer(photo)
            like_count = len(Like.objects.filter(photo=photo))
            return Response({'photo_data': serializer.data, 'like_data': like_count}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "failed to get photo"}, status=status.HTTP_400_BAD_REQUEST)


class LikePhoto(APIView):
    authentication_classes=[JWTAuthenticationSafe]
    def get(self, request, photo_id):
        try:
            photo = Photo.objects.get(id=photo_id)
            user = User.objects.get(id=request.headers['userid']) #request.headers 에서 가져올수 있나 지금?
            like_list = photo.like_set.filter(user = user)
            like = 0
            if like_list.count() > 0:
                photo.like_set.get(user=user).delete()
            else :
                Like.objects.create(user=user, photo=photo)
                like += 1
            return Response({'like' : like, 'success' : "like photo"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "failed to like photo"}, status=status.HTTP_400_BAD_REQUEST)

