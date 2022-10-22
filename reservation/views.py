import json
from tempfile import TemporaryFile
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from account.models import User
<<<<<<< HEAD
from reservation.serializers import ReservationSerializer, UserSerializer
from studio.models import AssginedTime
from reservation.models import Reservation
from rest_framework.response import Response
from rest_framework.views import APIView
=======
import reservation
from reservation.serializers import ReservationSerializer
from studio.models import AssignedTime
from reservation.models import Reservation
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
>>>>>>> 4e604bf7c70cc85757e8b27af508479639b7b6ab

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


# class ViewWithoutCSFRAuthentication(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(ViewWithoutCSFRAuthentication, self).dispatch(request, *args, **kwargs)


# status code 랑 JsonResponse 부분 다시 점검
# Create your views here.

# class ReservationCreateView(ViewWithoutCSFRAuthentication):
#     def post(self, request):
#         try:
#             body = json.loads(request.body)
#         except:
#             return JsonResponse({"error": "Invalid parameters"}, status = 400)
        
#         try:
#             user = User.objects.get(id=body['user_id'])
#             assigned_time = AssignedTime.objects.get(id = body['time_id'])
#             Reservation.objects.create(user=user, assigned_time=assigned_time, description=body['description'] )
#         except:
#             return JsonResponse({"error": "Failed to create Reservation"}, status = 400)
        
#         return JsonResponse({"success":"Reservation created successfully!"}, status = 201)

# class ReservationStateView(ViewWithoutCSFRAuthentication):
#     def post(self, request):
#         try:
#             body = json.loads(request.body)
#         except:
#             return JsonResponse({"error": "Invalid parameters"}, status = 400)

#         try:
#             user = User.objects.get(id=body['user_id'])
#             reservation = Reservation.objects.get(id=body['reservation_id'])
#             # 유저 그룹이 Normal group 인 유저는 액세스 불가 처리 .
#             if user.groups.filter(name='NormalUser'):
#                 if body['state'] == 'confirm':
#                     return JsonResponse({"error": "Unallowed Access for NormalUser"}, status = 403)
#                 else:
#                     reservation.state_change(body['state'])
#                 return JsonResponse({"success": f"reservation_{reservation.id}'s state is changed successfully."}, status =200)
#             else:
#                 # body['state'] 에는 confirmed, unconfirmed, canceled 정보가 필요함.
#                 reservation.state_change(body['state'])
#                 return JsonResponse({"success": f"reservation_{reservation.id}'s state is changed successfully."}, status =200)
#         except:
#             return JsonResponse({"error": "Failed to change reservation state"}, status=400)

class AllReservationView(APIView):
    def get(self, request): 
        try:
            user = User.objects.get(id=request.GET.get('user_id'))
            assigned_time = AssignedTime.objects.get(id=request.GET.get('assigned_time_id'))
            reservation = Reservation.objects.get(user=user, assigned_time=assigned_time)
            serializer = ReservationSerializer(reservation, many=True)
            return Response(serializer.data)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        try:
            user = User.objects.get(id=request.data.get('photographer_id'))
            assigned_time = AssignedTime.objects.get(id=request.data.get('assignedtime_id'))
            description = request.data.get('description')
            reservation = Reservation.objects.create(user=user, assigned_time=assigned_time, description=description)
            serializer = ReservationSerializer(reservation)
            return Response(serializer.data)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)      

class ReservationView(APIView):
    def get(self, request, id):
        try:
            reservation = Reservation.objects.get(id=id)
            serializer = ReservationSerializer(reservation)
            return Response(serializer.data)
        
<<<<<<< HEAD
        return JsonResponse({"success":"Reservation created successfully!"}, status = 201)    



class ReservationStateView(ViewWithoutCSFRAuthentication):
    def post(self, request):
        try:
            body = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid parameters"}, status = 400)

        try:
            user = User.objects.get(id=body['user_id'])
            reservation = Reservation.objects.get(id = body['user_id'])
            # 유저 그룹이 Normal group 인 유저는 액세스 불가 처리 .
            if user.groups.filter(name='NormalUser'):
                if body['state'] == 'confirm':
                    return JsonResponse({"error": "Unallowed Access for NormalUser"}, status = 403)
                else:
                    reservation.state_change(body['state'])
                return JsonResponse({"success": f"reservation_{reservation.id}'s state is changed successfully."}, status =200)
            else:
                # body['state'] 에는 confirmed, unconfirmed, canceled 정보가 필요함.
                reservation.state_change(body['state'])
                return JsonResponse({"success": f"reservation_{reservation.id}'s state is changed successfully."}, status =200)
        except:
            return JsonResponse({"error": "Failed to change reservation state"}, status=400)

class ReservationAllView(APIView):
    def get(self, request):
        try:
            body = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid parameters"}, status = 400)

        try:
            user = User.objects.get(id=body['user_id'])
            reservation = Reservation.objects.filter(user = user )
            ser=ReservationSerializer(reservation, many=True)
            return Response(ser.data)
        except:
            return JsonResponse({"error": "fail"}, status = 400)
    
class ReservationConfirmedView(APIView):
    def get(self, request):
        try:
            body = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid parameters"}, status = 400)

        try:
            user = User.objects.get(id=body['user_id'])
            reservation = Reservation.objects.filter(user = user.id, state=2)
            ser=ReservationSerializer(reservation, many=True)
            return Response(ser.data)
        except:
            return JsonResponse({"error": "fail"}, status = 400)

class ReservationCanceledView(APIView):
    def get(self, request):
        try:
            body = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid parameters"}, status = 400)

        try:
            user = User.objects.get(id=body['user_id'])
            reservation = Reservation.objects.filter(user = user.id, state=3)
            ser=ReservationSerializer(reservation, many=True)
            return Response(ser.data)
        except:
            return JsonResponse({"error": "fail"}, status = 400)

class ReservationUnconfirmedView(APIView):
    def get(self, request):
        try:
            body = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid parameters"}, status = 400)

        try:
            user = User.objects.get(id=body['user_id'])
            reservation = Reservation.objects.filter(user = user.id, state=1)
            ser=ReservationSerializer(reservation, many=True)
            return Response(ser.data)
        except:
            return JsonResponse({"error": "fail"}, status = 400)
=======
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 4e604bf7c70cc85757e8b27af508479639b7b6ab
