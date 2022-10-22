from django.urls import path
from reservation import views

app_name = 'reservation'
urlpatterns = [
<<<<<<< HEAD
    path("new/", views.ReservationCreateView.as_view(), name='create_reservation'),
    path("state/", views.ReservationStateView.as_view(), name='change_reservation_state'),
    path("getAll/", views.ReservationAllView.as_view(), name= 'get_reservation'),
    path("getConfirmed/", views.ReservationConfirmedView.as_view(), name= 'get_reservation')

=======
    path("reservation/", views.AllReservationView.as_view(), name='all_reservation'),
    # path("reservation/<int:id>", views.ReservationView.as_view(), name='reservation'),
>>>>>>> 4e604bf7c70cc85757e8b27af508479639b7b6ab
]
