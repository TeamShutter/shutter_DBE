from django.conf import settings
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from django.contrib.auth.models import Group
from accounts.authenticate import JWTAuthenticationSafe

from accounts.models import User
from .serializers import SignUpSerializer, LogInSerializer, LogOutSerializer, UserSerializer

from photo.models import Like, Photo
from photo.serializers import PhotoSerializer

from studio.models import Follow,Studio
from studio.serializers import StudioSerializer

from reservation.models import Reservation
from reservation.serializers import ReservationSerializer
class SignUpView(generics.GenericAPIView):
    authentication_classes = []
    serializer_class = SignUpSerializer
    def post(self, request):
        try:
            try: 
                user_info = request.data
            except:
                return Response({'error': 'failed to get data'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                serializer = self.serializer_class(data=user_info)
            except:
                return Response({'msg': "invalid data"}, status=status.HTTP_400_BAD_REQUEST)
            try:  
                serializer.is_valid(raise_exception = True)
            except:
                return Response({"msg": "validation fail"}, status=status.HTTP_400_BAD_REQUEST)
            try:
                serializer.save()
                return Response({ "msg": "user created" }, status=status.HTTP_201_CREATED)
            except:
                return Response({"error": "serializer save error"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'failed to signup user'}, status=status.HTTP_400_BAD_REQUEST)

class LogInView(generics.GenericAPIView):
    authentication_classes = []
    serializer_class = LogInSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        access_token = serializer.data["tokens"]["access"]
        refresh_token = serializer.data["tokens"]["refresh"]
        data = { "msg" : "login success", "username": serializer.data["username"] }
        res = Response(data, status=status.HTTP_200_OK)
        res.set_cookie('access_token', value=access_token, httponly=True)
        res.set_cookie('refresh_token', value=refresh_token, httponly=True)
        return res

class LogOutView(generics.GenericAPIView):
    serializer_class = LogOutSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        refresh_token = { "refresh" : request.COOKIES.get(settings.SIMPLE_JWT['REFRESH_TOKEN'])}
        serializer = self.serializer_class(data = refresh_token)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = { "msg": "logout success" }
        res = Response(data, status=status.HTTP_200_OK)
        res.delete_cookie('access_token')
        res.delete_cookie('refresh_token')
        return res

class LoadUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        try:
            user = request.user
            follow = Follow.objects.filter(user=user)
            like = Like.objects.filter(user=user)
            follow_studio = Studio.objects.filter(follow__in=follow)
            like_photo = Photo.objects.filter(like__in=like)
            reservation = Reservation.objects.filter(user=user)
            studio_serializer = StudioSerializer(follow_studio, many=True)
            photo_serializer = PhotoSerializer(like_photo, many=True)
            user_serializer = UserSerializer(user)
            reservation_serializer = ReservationSerializer(reservation, many=True)
            return Response(
                {'user_profile': user_serializer.data, 'photo': photo_serializer.data, 'studio': studio_serializer.data, 'reservation' : reservation_serializer.data},
                status=status.HTTP_200_OK
            )

        except:
            return Response(
                {'error': 'Something went wrong when loading user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserGroupView(generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes=[JWTAuthenticationSafe]
    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            studio_group, created =  Group.objects.get_or_create(name="StudioUser")
            normal_group, created =  Group.objects.get_or_create(name="NormalUser")
            group = request.data.get('group')
            
            if group == 'studio':
                user.groups.add(studio_group)
            else :
                user.groups.add(normal_group)
            return Response({'success': "user group assigned"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "failed to assign group"}, status=status.HTTP_400_BAD_REQUEST)


