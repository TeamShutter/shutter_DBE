from django.conf import settings
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from django.contrib.auth.models import Group
from .serializers import SignUpSerializer, LogInSerializer, LogOutSerializer, UserSerializer
from django.contrib.contenttypes.models import ContentType

class SignUpView(generics.GenericAPIView):
    authentication_classes = []
    serializer_class = SignUpSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        data = { "msg": "user created" }
        return Response(data, status=status.HTTP_201_CREATED)


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
    def get(self, request):
        try:
            studio_group, created =  Group.objects.get_or_create(name="Studio")
            user_id = request.user
            user_id.groups.add(studio_group)
            user = UserSerializer(user_id)
            
            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )

        except:
            return Response(
                {'error': 'Something went wrong when loading user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserGroupView(APIView):
    studio_group, created =  Group.objects.get_or_create(name="Studio")

    # content_type = ContentType.objects.get_for_model(Reservatio) 
