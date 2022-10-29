from django.urls import path
from .views import AllPhotoView, LikePhoto, PhotoView

urlpatterns = [
    path("", AllPhotoView.as_view(), name="all_photos"),
    path("<int:photo_id>/", PhotoView.as_view(), name='single_photo'),
    path("<int:photo_id>/like/", LikePhoto.as_view(), name="like_photo"),
]

