from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render

from accounts.authenticate import JWTAuthenticationSafe
from accounts.models import User
from photo.models import Photo
from photo.serializers import PhotoSerializer
from .models import AssignedTime, Follow, OpenedTime, Photographer, Place, Review, Studio, Product
from .serializers import OpenedTimeSerializer, PhotographerSerializer, PlaceSerializer, ReviewSerializer, StudioSerializer, ProductSerializer, AssignedTimeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json



class AllProductView(APIView):
    def get(self, request, studio_id):
        try:
            studio = Studio.objects.get(id=studio_id)
            product = Product.objects.filter(studio=studio)
            serializer = ProductSerializer(product, many=True)
            return Response({"data": serializer.data, "success" : "get all product"})
        
        except:
            return Response({"error" : "get all product"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, studio_id):
        try:
            studio = Studio.objects.get(id=studio_id)
            name = request.data.get('name')
            price = request.data.get('price')
            description = request.data.get('description')
            duration = request.data.get('duration')
            product = Product.objects.create(studio=studio, name=name, price=price, description=description, duration=duration)
            serializer = ProductSerializer(product)
            return Response({"data": serializer.data, "success" : "post product"})

        except:
            return Response({"error" : "post product"}, status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    # permission_classes = []  이거 어떻게 쓰는지 공부해봐야할듯-> 어떤 경우는 유저가 필요하고 어떤경우는 필요하지 않을텐데..
    def get(self, request, id, studio_id):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response({"data": serializer.data, "success" : "get product"})
            
        except:
            return Response({"error" : "get product"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id, studio_id): # put과 patch의 차이는 put은 전체수정, patch는 부분도 수정 가능의 의미
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product, data=request.data, partial=True) # partial=True 작성을 통해 부분만 수정 가능
            if serializer.is_valid(): # 이부분 없으니까 작동안했음.. 왜 그렇지??
                serializer.save()
                return Response({"data": serializer.data, "success" : "patch product"})
            
            return Response({"error" : "patch product invalid form"}, status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({"error" : "patch product"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id, studio_id):
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response({"success" : "delete product"}, status=status.HTTP_200_OK)
        
        except:
            return Response({"error" : "delete product"}, status=status.HTTP_400_BAD_REQUEST)



class AllPlaceView(APIView):
    def get(self, request, studio_id):
        try:
            studio = Studio.objects.get(id=studio_id)
            place = Place.objects.filter(studio=studio)
            serializer = PlaceSerializer(place, many=True)
            return Response({"data": serializer.data, "success" : "get all place"})
        
        except:
            return Response({"error" : "get all place"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, studio_id):
        try:
            studio = Studio.objects.get(id=studio_id)
            name = request.data.get('name')
            description = request.data.get('decription')
            address = request.data.get('address')
            place = Place.objects.create(studio=studio, name=name, description=description, address=address)
            serializer = PlaceSerializer(place)
            return Response({"data": serializer.data, "success" : "post place"})

        except:
            return Response({"error" : "post place"}, status=status.HTTP_400_BAD_REQUEST)

class PlaceView(APIView):
    def get(self, request, id, studio_id):
        try:
            place = Place.objects.get(id=id)
            serializer = PlaceSerializer(place)
            return Response({"data": serializer.data, "success" : "get place"})
            
        except:
            return Response({"error" : "get place"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id, studio_id):
        try:
            place = Place.objects.get(id=id)
            serializer = PlaceSerializer(place, data=request.data, partial=True) 
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success" : "patch place"})
            
            return Response({"error" : "patch place invalid form"}, status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({"error" : "patch place"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id, studio_id):
        try:
            place = Place.objects.get(id=id)
            place.delete()
            return Response({"success" : "delete place"}, status=status.HTTP_200_OK)
        
        except:
            return Response({"error" : "delete place"}, status=status.HTTP_400_BAD_REQUEST)

class AllOpenedTimeView(APIView):
    def get(self, request):
        try:
            studio = Studio.objects.get(id=request.GET.get('studio_id'))
            opened_time = OpenedTime.objects.filter(studio=studio)
            serializer = OpenedTimeSerializer(opened_time, many=True)
            return Response({"data": serializer.data, "success" : "get all opened_time"})
        
        except:
            return Response({"error" : "get all opened_time"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            studio = Studio.objects.get(id=request.data.get('studio_id'))
            date = request.data.get('date')
            hour = request.data.get('hour')
            minute = request.data.get('minute')
            opened_time = OpenedTime.objects.create(studio=studio, date=date, hour=hour, minute=minute)
            serializer = OpenedTimeSerializer(opened_time)
            return Response({"data": serializer.data, "success" : "post opened_time"})

        except:
            return Response({"error" : "post opened_time"}, status=status.HTTP_400_BAD_REQUEST)

class OpenedTimeView(APIView):
    def get(self, request, id):
        try:
            opened_time = OpenedTime.objects.get(id=id)
            serializer = OpenedTimeSerializer(opened_time)
            return Response({"data": serializer.data, "success" : "get opened_time"})
            
        except:
            return Response({"error" : "get opened_time"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            opened_time = OpenedTime.objects.get(id=id)
            serializer = OpenedTimeSerializer(opened_time, data=request.data, partial=True) 
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success" : "patch opened_time"})
            
            return Response({"error" : "patch opened_time invalid form"}, status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({"error" : "patch opened_time"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            opened_time = OpenedTime.objects.get(id=id)
            opened_time.delete()
            return Response({"success" : "delete opened_time"}, status=status.HTTP_200_OK)
        
        except:
            return Response({"error" : "delete opened_time"}, status=status.HTTP_400_BAD_REQUEST)


            
class AllPhotographerView(APIView):
    def get(self, request, studio_id):
        try:
            studio = Studio.objects.get(id=studio_id)
            photographer = Photographer.objects.filter(studio=studio)
            serializer = PhotographerSerializer(photographer, many=True)
            return Response({"data": serializer.data, "success" : "get all photographer"})
        
        except:
            return Response({"error" : "get all photographer"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, studio_id):
        try:
            studio = Studio.objects.get(id=studio_id)
            name = request.data.get('name')
            photographer = Photographer.objects.create(studio=studio, name=name)
            serializer = PhotographerSerializer(photographer)
            return Response({"data": serializer.data, "success" : "post photographer"})

        except:
            return Response({"error" : "post photographer"}, status=status.HTTP_400_BAD_REQUEST)

class PhotographerView(APIView):
    def get(self, request, id, studio_id):
        try:
            photographer = Photographer.objects.get(id=id)
            serializer = PhotographerSerializer(photographer)
            return Response({"data": serializer.data, "success" : "get photographer"})
            
        except:
            return Response({"error" : "get photographer"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id, studio_id):
        try:
            photographer = Photographer.objects.get(id=id)
            serializer = PhotographerSerializer(photographer, data=request.data, partial=True) 
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success" : "patch photographer"})
            
            return Response({"error" : "patch photographer invalid form"}, status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({"error" : "patch photographer"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id, studio_id):
        try:
            photographer = Photographer.objects.get(id=id)
            photographer.delete()
            return Response({"success" : "delete photographer"}, status=status.HTTP_200_OK)
        
        except:
            return Response({"error" : "delete photographer"}, status=status.HTTP_400_BAD_REQUEST)


class AllAssignedTimeView(APIView):
    def get(self, request): 
        try:
            photographer = Photographer.objects.get(id=request.GET.get('photographer_id'))
            assigned_time = AssignedTime.objects.filter(photographer=photographer)
            serializer = AssignedTimeSerializer(assigned_time, many=True)
            return Response(serializer.data)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, studio_id):
        try:
            photographer = Photographer.objects.get(id=request.data.get('photographer_id'))
            opened_time = OpenedTime.objects.get(id=request.data.get('assigned_time_id'))
            assigned_time = AssignedTime.objects.create(photographer=photographer, opened_time=opened_time)
            serializer = AssignedTimeSerializer(assigned_time)
            return Response(serializer.data)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AllStudioView(APIView):
    authentication_classes=[JWTAuthenticationSafe]

    def get(self, request):
        if not request.data.get('town'):
            try:
                studios = Studio.objects.all()
                serializer = StudioSerializer(studios, many=True)
                return Response({"data" : serializer.data, "success": "get all studios"})
            except:
                return Response({"error": "failed to get all studios"},status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                town = request.data.get('town')
                studios = Studio.objects.filter(town=town)
                serializer = StudioSerializer(studios, many=True)
                return Response({"data" : serializer.data, "success": "get all town's studios"})
            except:
                return Response({"error": "failed to get town's studios"},status=status.HTTP_400_BAD_REQUEST)

                
class StudioView(APIView):
    authentication_classes=[JWTAuthenticationSafe]
    def get(self, request, studio_id):
        try:
            studio = Studio.objects.get(id=studio_id)
            photos = Photo.objects.filter(studio_id=studio_id)
            
            studio_serializer = StudioSerializer(studio)
            photo_serializer = PhotoSerializer(photos, many= True)
            return Response({"studio_data" : studio_serializer.data, "photo_data" : photo_serializer.data, "success": "get studio"})
        except:
            return Response({"error": "failed to get studio infos."},status=status.HTTP_400_BAD_REQUEST)

class AllStudioReview(APIView):
    authentication_classes=[JWTAuthenticationSafe]
    def get(self, request, studio_id):
        try:
            studio = Studio.objects.get(id=studio_id)
            review = Review.objects.filter(studio=studio)
            serializer = ReviewSerializer(review, many=True)
            return Response({"data" : serializer.data, "success" : "get studio review"})
        except:
            return Response({"error": "failed to get studio review"},status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, studio_id):
        try:
            content = request.data.get('content')
            rating = request.data.get('rating')
            user = User.objects.get(id=request.headers['userid']) # userid 받는 방법이 왜 다른거지??
            review = Review.objects.create(studio_id = studio_id, content=content, author=user, rating=rating)
            serializer = ReviewSerializer(review)
            return Response({"data" : serializer.data, "success" : "post studio review"})
        except:
            return Response({"error": "failed to post studio review"},status=status.HTTP_400_BAD_REQUEST)

class StudioReview(APIView):
    authentication_classes=[JWTAuthenticationSafe]
    def patch(self, request, studio_id, id):
        try:
            review = Review.objects.get(id=id)
            serializer = ReviewSerializer(review, data=request.data, partial=True) 
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success" : "patch studio review"})
            return Response({"error" : "patch studio review invalid form"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "failed to patch studio review"},status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, studio_id, id):
        try:
            review = Review.objects.get(id=id)
            review.delete()
            return Response({"success" : "delete studio review"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "failed to delete studio review"},status=status.HTTP_400_BAD_REQUEST)
    
class FollowStudio(APIView):
    authentication_classes=[JWTAuthenticationSafe]
    
    def get(self, request, studio_id):
        try:
            studio = Studio.objects.get(id=studio_id)
            user = User.objects.get(id=request.headers['userid'])
            follow_list = studio.follow_set.filter(user = user)
            follow = 0
            if follow_list.count() > 0:
                studio.like_set.get(user=user).delete()
            else :
                Follow.objects.create(user=user, studio=studio)
                follow += 1
            return Response({'follow' : follow, 'success' : "follow studio"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "failed to follow studio"}, status=status.HTTP_400_BAD_REQUEST)