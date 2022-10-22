from django.urls import path
from reservation import views

app_name = 'reservation'
urlpatterns = [
    path("reservation/", views.AllReservationView.as_view(), name='all_reservation'),
    # path("reservation/<int:id>", views.ReservationView.as_view(), name='reservation'),
]
