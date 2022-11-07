from django.urls import path
from .views import AllTagView

app_name= 'tags'
urlpatterns =[
    path('', AllTagView.as_view(), name="get_all_tag")
]