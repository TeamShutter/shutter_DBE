from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render
from .models import Studio, Product
import json

def studio_inst_to_dict(studio_inst):
    result = {}
    result['id'] = studio_inst.id
    result['name'] = studio_inst.name
    return result

# Create your views here.
class StudioListView(View):
    def get(self, request):
        try:
            studio_list = []
            studio_queryset = Studio.objects.all()
            for studio_inst in studio_queryset:
                studio_list.append(
                    studio_inst_to_dict(studio_inst)
                )
            data = {"studios": studio_list}
            return JsonResponse(data, status=200)
        except:
            return JsonResponse({"msg": "Failed to get studios"}, status =404)



# class StudioCreateView(View):
#     def post(self, request):
#         try:
#             body = json.loads(request.body)
#         except:
#             return JsonResponse({"msg": "Invalid parameters"}, status =400)
#         try:
#             studio_inst = Studio.objects.
