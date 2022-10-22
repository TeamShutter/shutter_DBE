import json
from tempfile import TemporaryFile
from django.http import JsonResponse
from django.shortcuts import render
from account.models import User
import reservation
from reservation import serializers
from reservation.serializers import ReservationSerializer
from studio.models import AssignedTime, OpenedTime, Photographer, Product, Studio
from reservation.models import Reservation
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class AllReservationView(APIView):
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
            user = User.objects.get(id=request.data.get('photographer_id'))
            assigned_time = AssignedTime.objects.get(id=request.data.get('assignedtime_id'))
            description = request.data.get('description')
            reservation = Reservation.objects.create(user=user, assigned_time=assigned_time, description=description)
            reservation.assigned_time.update_available()
            serializer = ReservationSerializer(reservation)
            return Response({'data' : serializer.data, 'success' : 'post reservation'})
        
        except:
            return Response({'error' : 'post reservation'}, status=status.HTTP_400_BAD_REQUEST)      

class ReservationView(APIView):
    def get(self, request, id, studio_id):
        try:
            reservation = Reservation.objects.get(id=id)
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
    
