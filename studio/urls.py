from django.urls import path
from studio import views

app_name = 'studio'
urlpatterns = [
    path("", views.StudioListView.as_view(), name='studio_list'),
    
]

# photo id = pid
