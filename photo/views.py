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
            photos = Photo.objects.all()
            serializer = PhotoSerializer(photos, many=True)
            return Response({"data" : serializer.data, "success": "get all photos"})
        except:
            return Response({"error": "failed to get all photos"},status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def GetAllPhotos(request):
#     paginator = PageNumberPagination()
#     paginator.page_size = 100
#     if request.GET.get('studioId') and request.GET.get('studioId') != '0':
#         studioId = request.GET.get('studioId')
#         allPhotos = Photo.objects.filter(studio = studioId)
#         serializer = PhotoByStudioSerializer(allPhotos, many=True)
#     else:
#         allPhotos = Photo.objects.all()
#         if request.GET.get('price') and request.GET.get('price') != '0':
#             studios = Studio.objects.filter(price = request.GET.get('price'))
#             allPhotos = allPhotos.filter(studio__in = studios)
#         # if request.GET.get('tags') and request.GET.get('tags') != '0':
#         #     id_list = id=request.GET.getlist('tags')
#         #     for id in id_list:
#         #         tags = Tag.objects.filter(id=id)
#         #         allPhotos = allPhotos.filter(tags__in=tags)
#         if request.GET.get('sex') and request.GET.get('sex') != '0':
#             allPhotos = allPhotos.filter(sex=request.GET.get('sex'))
#         if request.GET.get('town') and request.GET.get('town') != '0':
#             studios = Studio.objects.filter(town = request.GET.get('town'))
#             allPhotos = allPhotos.filter(studio__in = studios)
#         if request.GET.get('photoshop') and request.GET.get('photoshop') != '0':
#             studios = Studio.objects.filter(photoshop = request.GET.get('photoshop'))
#             allPhotos = allPhotos.filter(studio__in = studios)
    
#     result_page = paginator.paginate_queryset(allPhotos, request)
#     serializer = PhotoSerializer(result_page, many=True)
#     return Response(serializer.data)
# class PhotoView(APIView):
#     authentication_classes=[JWTAuthenticationSafe]
#     def 


@api_view(['GET'])
def GetPhoto(request, pid):
    photo = Photo.objects.get(id=pid)
    serializer = PhotoSerializer(photo)
    like_count = len(Like.objects.filter(photo=photo))
    return Response(serializer.data)

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

