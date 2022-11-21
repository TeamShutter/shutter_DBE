from django.urls import path
from .views import AllPhotoView, LikePhotoView, PhotoView, RelatedPhotoView

urlpatterns = [
    path("", AllPhotoView.as_view(), name="all_photos"),
    path("<int:photo_id>/", PhotoView.as_view(), name='single_photo'),
    path("<int:photo_id>/like/", LikePhotoView.as_view(), name='like_photo'),
    # path("color/", PhotoColorView.as_view(), name="all_colors"),
    path("<int:photo_id>/related_photos/", RelatedPhotoView.as_view(), name='related_photos'),
]

