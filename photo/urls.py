from django.urls import path, include
from .views import GetAllPhotos, GetPhoto, LikePhoto

urlpatterns = [
    path("", GetAllPhotos),
    path("<int:pid>/", GetPhoto),
    path("<int:pid>/like/", LikePhoto)
]

