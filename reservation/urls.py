from django.urls import path
from reservation import views

app_name = 'reservation'
urlpatterns = [
    path("new/", views.ReservationCreateView.as_view(), name='create_reservation'),
    path("state/", views.ReservationStateView.as_view(), name='change_reservation_state'),
]
