from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.models import User
from studio.models import Studio
from .models import Photo, Like
from .serializers import PhotoByStudioSerializer, PhotoSerializer
from studio.serializers import StudioSerializer
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from account.authenticate import JWTAuthenticationSafe
# Create your views here.

class AllPhotoView(APIView):
    authentication_classes=[JWTAuthenticationSafe]
    def get(self, request):
        try:
            paginator = PageNumberPagination()
            paginator.page_size = 60
            photos = Photo.objects.all()
            result_photos = paginator.paginate_queryset(photos, request)
            serializer = PhotoSerializer(result_photos, many=True)
            
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
            return Response({"error": "failed to get photo"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def LikePhoto(request, pid):
    photo = Photo.objects.get(id=pid)
    # photo 에 좋아요 누른 사람들의 리스트를 갖고옴
    user = User.objects.get(id=request.headers['userid'])
    like_list = photo.like_set.filter(user = user)
    
    # 리스트에 좋아요 버튼을 누른 사람의 id가 있으면 delete, 없으면 like 생성.
    like = 0
    if like_list.count() > 0:
        photo.like_set.get(user=user).delete()
    else :
        Like.objects.create(user=user, photo=photo)
        like += 1
    return Response({'like' : like})

class LikePhotoView(APIView):
    authentication_classes=[JWTAuthenticationSafe]
    def post(self, request, photo_id):  
        try:
            photo = Photo.objects.get(id=photo_id)
            user = request.user
            user_like_list = photo.like_set.filter(user = user)

            if user_like_list.count() > 0:
                photo.like_set.get(user=user).delete()
            else:
                Like.objects.create(user=user, photo=photo)
            return Response({"success": "like action is completed"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "like failed.. "}, status=status.HTTP_400_BAD_REQUEST)

