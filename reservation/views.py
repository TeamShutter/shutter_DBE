import json
from tempfile import TemporaryFile
from django.http import JsonResponse
from django.shortcuts import render
from accounts.models import User
from accounts.permissions import UserReadOnlyStudioAll
import rest_framework
import reservation
from reservation import serializers
from reservation.serializers import ReservationSerializer
from studio.models import AssignedTime, Place, Product, Studio
from reservation.models import Reservation
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# @csrf_exempt
class AllStudioReservationView(APIView):
    permission_classes = [rest_framework.permissions.IsAuthenticated]
    def get(self, request, studio_id): 
        try:
            studio = Studio.objects.get(id=studio_id)
            reservation = Reservation.objects.get(studio=studio)
            if(request.data.get('state')):
                try:
                    state = request.data.get('state')
                    reservation = reservation.objects.filter(state=state)
                except:
                    return Response({'error' : "fail to get reservation by state"}, status=status.HTTP_400_BAD_REQUEST)
            if(request.data.get('place_id')):
                try:
                    place = Place.objects.get(id=request.data.get('place_id'))
                    reservation = reservation.objects.filter(place=place)
                except:
                    return Response({'error' : "fail to get reservation by place"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = ReservationSerializer(reservation, many=True)
            return Response({'data' : serializer.data, 'success' : 'get all reservation'})
        
        except:
            return Response({'error' : 'get all reservation'}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, studio_id):
        try:
            user = request.user
            print(request.data)
            for req in request.data:
                print(studio_id)
                assigned_time_id = request.data.get(f"{req}").get("assigned_time_id")
                product_id = request.data.get(req).get("product_id")
                assigned_time = AssignedTime.objects.get(id=assigned_time_id)
                product = Product.objects.get(id=product_id)
                reservation = Reservation.objects.create(user = user,assigned_time=assigned_time, product=product)
                reservation.assigned_time.update_available()
                serializers = ReservationSerializer(reservation)
                print(serializers.data)
            return Response({'success' : 'reservation created!'}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({'error' : 'post reservation'}, status=status.HTTP_400_BAD_REQUEST)      

class StudioReservationView(APIView):
    permission_classes = [UserReadOnlyStudioAll]
    def get(self, request, studio_id, reservation_id):
        try:
            reservation = Reservation.objects.get(id=reservation_id)
            serializer = ReservationSerializer(reservation)
            return Response({'data' : serializer.data, 'success' : 'get reservation'})
        
        except:
            return Response({'error' : 'get reservation'}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id, studio_id):
        try:
            reservation = Reservation.objects.get(id=id)
            if request.data["state"] == 3:
                reservation.assigned_time.update_available()
                reservation.delete()
            
            serializer = ReservationSerializer(reservation, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": "reservation changed"})
            
            return Response({'error' : 'patch reservation invalid form'}, status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({'error' : 'patch reservation'}, status=status.HTTP_404_NOT_FOUND)
    
class AllAdminReservationView(APIView):
    # permission_classes = [rest_framework.permissions.IsAdminUser]
    def get(self, request):
        all_reservations = Reservation.objects.all()
        reservation_ser = ReservationSerializer(all_reservations, many=True)
        return Response({"data":reservation_ser.data}, status=status.HTTP_200_OK)

class AdminReservationView(APIView):
    # permission_classes = [rest_framework.permissions.IsAdminUser]
    def patch(self, request, reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        reservation_ser = ReservationSerializer(reservation, data=request.data, partial=True)
        reservation_ser.is_valid()
        reservation_ser.save()
        return Response({"data":reservation_ser.data}, status=status.HTTP_200_OK)
    