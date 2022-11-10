from django.shortcuts import render
from rest_framework.views import APIView
from .models import Tag
from .serializers import TagSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class AllTagView(APIView):
    def get(self, request):
        try:
            tag = Tag.objects.all()
            serializer = TagSerializer(tag, many=True)
            return Response({"data" : serializer.data, "success": "get all tags"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "failed to get all tags"}, status=status.HTTP_400_BAD_REQUEST)


