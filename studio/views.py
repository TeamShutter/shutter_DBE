from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render
from .models import AssignedTime, OpenedTime, Photographer, Studio, Product
from .serializers import OpenedTimeSerializer, PhotographerSerializer, StudioSerializer, ProductSerializer, AssignedTimeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json

# def studio_inst_to_dict(studio_inst):
#     result = {}
#     result['id'] = studio_inst.id
#     result['name'] = studio_inst.name
#     return result

# class StudioListView(APIView):
#     def get(self, request):
#         try:
#             studio_list = []
#             studio_queryset = Studio.objects.all()
#             for studio_inst in studio_queryset:
#                 studio_list.append(
#                     studio_inst_to_dict(studio_inst)
#                 )
#             data = {"studios": studio_list}
#             return JsonResponse(data, status=200)
#         except:
#             return JsonResponse({"msg": "Failed to get studios"}, status =404)



# class StudioCreateView(View):
#     def post(self, request):
#         try:
#             body = json.loads(request.body)
#         except:
#             return JsonResponse({"msg": "Invalid parameters"}, status =400)
#         try:
#             studio_inst = Studio.objects.

class AllProductView(APIView):
    def get(self, request):
        try:
            studio = Studio.objects.get(id=request.GET.get('studio_id'))
            product = Product.objects.filter(studio=studio)
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        # 이 부분은 body에 raw data로 집어넣을때
        # try:
        #     data = json.loads(request.body)
        #     studio = Studio.objects.get(id=data['studioId'])
        #     name = data['name']
        #     price = data['price']
        #     description = data['description']
        #     duration = data['duration']
        #     product = Product.objects.create(studio=studio, name=name, price=price, description=description, duration=duration)
        #     print(product)
        #     serializer = ProductSerializer(product)
        #     return Response(serializer.data)
        try:
            studio = Studio.objects.get(id=request.data.get('studio_id'))
            name = request.data.get('name')
            price = request.data.get('price')
            description = request.data.get('description')
            duration = request.data.get('duration')
            product = Product.objects.create(studio=studio, name=name, price=price, description=description, duration=duration)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    # permission_classes = []  이거 어떻게 쓰는지 공부해봐야할듯-> 어떤 경우는 유저가 필요하고 어떤경우는 필요하지 않을텐데..
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
            
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id): # put과 patch의 차이는 put은 전체수정, patch는 부분도 수정 가능의 의미
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product, data=request.data, partial=True) # partial=True 작성을 통해 부분만 수정 가능
            if serializer.is_valid(): # 이부분 없으니까 작동안했음.. 왜 그렇지??
                serializer.save()
                return Response(serializer.data)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response(status=status.HTTP_200_OK)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AllOpenedTimeView(APIView):
    def get(self, request):
        try:
            studio = Studio.objects.get(id=request.GET.get('studio_id'))
            opened_time = OpenedTime.objects.filter(studio=studio)
            serializer = OpenedTimeSerializer(opened_time, many=True)
            return Response(serializer.data)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            studio = Studio.objects.get(id=request.data.get('studio_id'))
            date = request.data.get('date')
            hour = request.data.get('hour')
            minute = request.data.get('minute')
            opened_time = OpenedTime.objects.create(studio=studio, date=date, hour=hour, minute=minute)
            serializer = OpenedTimeSerializer(opened_time)
            return Response(serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class OpenedTimeView(APIView):
    def get(self, request, id):
        try:
            opened_time = OpenedTime.objects.get(id=id)
            serializer = OpenedTimeSerializer(opened_time)
            return Response(serializer.data)
            
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            opened_time = OpenedTime.objects.get(id=id)
            serializer = OpenedTimeSerializer(opened_time, data=request.data, partial=True) 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            opened_time = OpenedTime.objects.get(id=id)
            opened_time.delete()
            return Response(status=status.HTTP_200_OK)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


            
class AllPhotographerView(APIView):
    def get(self, request):
        try:
            studio = Studio.objects.get(id=request.GET.get('studio_id'))
            photographer = Photographer.objects.filter(studio=studio)
            serializer = PhotographerSerializer(photographer, many=True)
            return Response(serializer.data)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            studio = Studio.objects.get(id=request.data.get('studio_id'))
            name = request.data.get('name')
            photographer = Photographer.objects.create(studio=studio, name=name)
            serializer = PhotographerSerializer(photographer)
            return Response(serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PhotographerView(APIView):
    def get(self, request, id):
        try:
            photographer = Photographer.objects.get(id=id)
            serializer = PhotographerSerializer(photographer)
            return Response(serializer.data)
            
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        try:
            photographer = Photographer.objects.get(id=id)
            serializer = PhotographerSerializer(photographer, data=request.data, partial=True) 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            photographer = Photographer.objects.get(id=id)
            photographer.delete()
            return Response(status=status.HTTP_200_OK)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AllAssignedTimeView(APIView):
    def get(self, request): 
        try:
            photographer = Photographer.objects.get(id=request.GET.get('photographer_id'))
            assigned_time = AssignedTime.objects.filter(photographer=photographer)
            serializer = AssignedTimeSerializer(assigned_time, many=True)
            return Response(serializer.data)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        try:
            photographer = Photographer.objects.get(id=request.data.get('photographer_id'))
            opened_time = OpenedTime.objects.get(id=request.data.get('assigned_time_id'))
            assigned_time = AssignedTime.objects.create(photographer=photographer, opened_time=opened_time)
            serializer = AssignedTimeSerializer(assigned_time)
            return Response(serializer.data)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AssignedTimeView(APIView):
    def get(self, request):
        try:
            return

        except:
            return