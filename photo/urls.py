from django.urls import path
from .views import AllPhotoView

urlpatterns = [
    path("", AllPhotoView.as_view(), name="all_photos"),
    # path("<int:pid>/", GetPhoto),
    # path("<int:pid>/like/", LikePhoto)
]

