import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from account.models import User
from reservation.serializers import ReservationSerializer
from studio.models import AssginedTime
from reservation.models import Reservation

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


class ViewWithoutCSFRAuthentication(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ViewWithoutCSFRAuthentication, self).dispatch(request, *args, **kwargs)


# status code 랑 JsonResponse 부분 다시 점검
# Create your views here.
class ReservationCreateView(ViewWithoutCSFRAuthentication):
    def post(self, request):
        try:
            body = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid parameters"}, status = 400)
        
        try:
            user = User.objects.get(id=body['user_id'])
            assigned_time = AssginedTime.objects.get(id = body['time_id'])
            Reservation.objects.create(user=user, assigned_time=assigned_time, description=body['description'] )
        except:
            return JsonResponse({"error": "Failed to create Reservation"}, status = 400)
        
        return JsonResponse({"success":"Reservation created successfully!"}, status = 201)

class ReservationStateView(ViewWithoutCSFRAuthentication):
    def post(self, request):
        try:
            body = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid parameters"}, status = 400)

        try:
            user = User.objects.get(id=body['user_id'])
            reservation = Reservation.objects.get(id=body['reservation_id'])
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
