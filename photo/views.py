from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.models import User
from accounts.permissions import StudioReadOnlyUserAll
from studio.models import Studio
from .models import Photo, Like
from tags.models import Tag
from .serializers import PhotoSerializer
from studio.serializers import StudioSerializer
from django.contrib.auth.models import User
from accounts.authenticate import JWTAuthenticationSafe
from itertools import combinations
# Create your views here.
class AllPhotoView(APIView):
    authentication_classes=[JWTAuthenticationSafe]

    def get(self, request):
        try:
            if request.GET.get('studio_id'):
                studio = Studio.objects.get(id=request.GET.get('studio_id'))
                photo = Photo.objects.filter(studio=studio)
            else:
                # photo = Photo.objects.order_by('?').all() : Todo -> 사진 랜덤으로 보여주기
                photo = Photo.objects.all()
                if request.GET.get('tags') and request.GET.get('tags') != '0':
                    tags_id = request.GET.getlist('tags')
                    for tag_id in tags_id:
                        tags = Tag.objects.filter(id=tag_id)
                        photo = photo.filter(tags__in=tags)                
                if request.GET.get('town') and request.GET.get('town') != '0':
                    studios = Studio.objects.filter(town = request.GET.get('town'))
                    photo = photo.filter(studio__in = studios)
                if request.GET.get('max_price') and request.GET.get('max_price') != "0":
                    photo = photo.filter(price__lte = request.GET.get('max_price'))
                if request.GET.get('min_price') and request.GET.get('min_price') != "0":
                    photo = photo.filter(price__gte = request.GET.get('min_price'))
                if request.GET.get('color') and request.GET.get('color') != "0":
                    photo = photo.filter(color = request.GET.get('color'))
                if request.GET.get('photoType') and request.GET.get('photoType') != "0":
                    photo = photo.filter(type= request.GET.get('photoType'))
            serializer = PhotoSerializer(photo, many=True)        
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
    def patch(self, request, photo_id):
        try:
            photo = Photo.objects.get(id = photo_id)
            serializer = PhotoSerializer(photo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": "photo changed"})
            return Response({'error' : 'patch reservation invalid form'}, status=status.HTTP_400_BAD_REQUEST)
            return
        except:
            return Response({"error": "failed to patch photo"},status=status.HTTP_400_BAD_REQUEST)




class LikePhotoView(APIView):
    permission_classes = [StudioReadOnlyUserAll]
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


# color를 원래대로 설정 안하고 추가한 이름대로 보여주고 싶을때

# class PhotoColorView(APIView):
#     authentication_classes=[JWTAuthenticationSafe]
#     def get(self, request):
#         try:
#             photo = Photo.objects.all()
#             color = []
#             for i in range(len(photo)):
#                 if photo.values()[i]['color'] not in color:
#                     color.append(photo.values()[i]['color'])
#             return Response({'data' : color}, status=status.HTTP_200_OK)
#         except:
#             return Response({"error": "failed to get color"}, status=status.HTTP_400_BAD_REQUEST)


# 연관된 사진들 (태그 2개 이상 곂칠때로 일단 설정)
class RelatedPhotoView(APIView):
    authentication_classes=[JWTAuthenticationSafe]
    def get(self, reqeust, photo_id):
        try:
            photo = Photo.objects.filter(id=photo_id)
            tags = Tag.objects.filter(photos__in = photo)
            all_photos = Photo.objects.all()
            related_photo_list = []
            tag_sets = list(combinations(tags, 2))
            for tag_set in tag_sets:
                related_photos = all_photos.filter(tags__in = tag_set)
                related_photo_list.append(related_photos)
            print(related_photo_list)

            serializer = PhotoSerializer(related_photo_list, many=True)
            return Response({"success": "get all photos"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "failed to get related photos"}, status=status.HTTP_400_BAD_REQUEST)
