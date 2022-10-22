from django.urls import path

from reservation.views import AllReservationView, ReservationView
from .views import AllPlaceView, AssignedTimeView, AllAssignedTimeView, AllPhotographerView, PhotographerView, AllProductView, PlaceView, ProductView, AllOpenedTimeView, OpenedTimeView
# from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'studio'
urlpatterns = [
    path('<int:studio_id>/product/', AllProductView.as_view(), name='product_list'),
    path('<int:studio_id>/product/<int:id>/', ProductView.as_view(), name='product'),
    path('<int:studio_id>/place/', AllPlaceView.as_view(), name='place_list'),
    path('<int:studio_id>/place/<int:id>/', PlaceView.as_view(), name='place'),
    path('openedtime/', AllOpenedTimeView.as_view(), name='opened_time_list'),
    path('openedtime/<int:id>/', OpenedTimeView.as_view(), name='opened_time'),
    path('<int:studio_id>/photographer/', AllPhotographerView.as_view(), name='photographer_list'),
    path('<int:studio_id>/photographer/<int:id>/', PhotographerView.as_view(), name='photographer'),
    path('<int:studio_id>/reservation/', AllReservationView.as_view(), name='studio_reservation_list'),
    path('<int:studio_id>/reservation/<int:id>/', ReservationView.as_view(), name='studio_reservation'),
    # path('assignedtime/', AllAssignedTimeView.as_view(), name='assigned_time_list'),
    # path('assignedtime/<int:id>/', AssignedTimeView.as_view(), name='assigned_time'),
    
]

# urlpatterns = format_suffix_patterns(urlpatterns)
