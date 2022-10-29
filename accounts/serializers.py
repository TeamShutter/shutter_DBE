from pyexpat import model
from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
import re

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password']
    
    def validate_name(self, attrs):
        email = attrs.get('email', '')
        email_type = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if email_type.match(email) == None:
            raise serializers.ValidationError(self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LogInSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=4)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user =  User.objects.get(username=obj['email'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['password', 'email', 'tokens']
    
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('user not active')

        return {
            'email': user.email,
            'tokens': user.tokens
        }

class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            msg = 'Token is blacklisted'
            raise serializers.ValidationError(msg, code='authorization')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'groups']
