from django.urls import path
from .views import AllStudioReview, AllStudioView, FollowStudio, StudioReview, StudioView
from reservation.views import AllStudioReservationView, StudioReservationView
from .views import AllPlaceView, AllAssignedTimeView, AllPhotographerView, PhotographerView, AllProductView, PlaceView, ProductView, AllOpenedTimeView, OpenedTimeView
# from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'studio'
urlpatterns = [
    path("", AllStudioView.as_view(), name="all_studios"),
    path("<int:studio_id>/", StudioView.as_view(), name="studio"),
    path('<int:studio_id>/product/', AllProductView.as_view(), name='product_list'),
    path('<int:studio_id>/product/<int:id>/', ProductView.as_view(), name='product'),
    path('<int:studio_id>/place/', AllPlaceView.as_view(), name='place_list'),
    path('<int:studio_id>/place/<int:id>/', PlaceView.as_view(), name='place'),
    path('openedtime/', AllOpenedTimeView.as_view(), name='opened_time_list'),
    path('openedtime/<int:id>/', OpenedTimeView.as_view(), name='opened_time'),
    path('<int:studio_id>/photographer/', AllPhotographerView.as_view(), name='photographer_list'),
    path('<int:studio_id>/photographer/<int:id>/', PhotographerView.as_view(), name='photographer'),
    path('<int:studio_id>/reservation/', AllStudioReservationView.as_view(), name='studio_reservation_list'),
    path('<int:studio_id>/reservation/<int:id>/', StudioReservationView.as_view(), name='studio_reservation'),
    path('<int:studio_id>/assignedtime/', AllAssignedTimeView.as_view(), name='assigned_time_list'),
    # path('assignedtime/<int:id>/', AssignedTimeView.as_view(), name='assigned_time'),
    path('<int:studio_id>/review/', AllStudioReview.as_view(), name='studio_review_list'),
    path('<int:studio_id>/review/<int:id>/', StudioReview.as_view(), name='studio_review'),
    path('<int:studio_id>/follow/', FollowStudio.as_view(), name='follow_studio'),
]

