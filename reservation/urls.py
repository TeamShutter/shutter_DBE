from django.urls import path
from reservation.views import AllStudioReservationView, StudioReservationView, AllAdminReservationView, AdminReservationView
# from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'reservation'
urlpatterns = [
    path("", AllAdminReservationView.as_view(), name="reservation_view"),
    path("<int:reservation_id>/", AdminReservationView.as_view(), name="reservation_patch"),
]