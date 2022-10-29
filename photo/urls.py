from django.urls import path
<<<<<<< HEAD
from .views import AllPhotoView, LikePhotoView, PhotoView
=======
from .views import AllPhotoView, LikePhoto, PhotoView
>>>>>>> 9ed56a8a9c5546af68682568561751109e2f59c3

urlpatterns = [
    path("", AllPhotoView.as_view(), name="all_photos"),
    path("<int:photo_id>/", PhotoView.as_view(), name='single_photo'),
<<<<<<< HEAD
    path("<int:photo_id>/like/", LikePhotoView.as_view(), name='like_photo'),
=======
    path("<int:photo_id>/like/", LikePhoto.as_view(), name="like_photo"),
>>>>>>> 9ed56a8a9c5546af68682568561751109e2f59c3
]

