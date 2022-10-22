from django.urls import path
from reservation import views

app_name = 'reservation'
urlpatterns = [
    path("new/", views.ReservationCreateView.as_view(), name='create_reservation'),
    path("state/", views.ReservationStateView.as_view(), name='change_reservation_state'),
    path("getAll/", views.ReservationAllView.as_view(), name= 'get_reservation'),
    path("getConfirmed/", views.ReservationConfirmedView.as_view(), name= 'get_reservation')

]
