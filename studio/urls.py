from django.urls import path
from .views import AssignedTimeView, AllAssignedTimeView, AllPhotographerView, PhotographerView, AllProductView, ProductView, AllOpenedTimeView, OpenedTimeView
# from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'studio'
urlpatterns = [
    path('product/', AllProductView.as_view(), name='product_list'),
    path('product/<int:id>/', ProductView.as_view(), name='product'),
    path('openedtime/', AllOpenedTimeView.as_view(), name='opened_time_list'),
    path('openedtime/<int:id>/', OpenedTimeView.as_view(), name='opened_time'),
    path('photographer/', AllPhotographerView.as_view(), name='photographer_list'),
    path('photographer/<int:id>/', PhotographerView.as_view(), name='photographer'),
    path('assignedtime/', AllAssignedTimeView.as_view(), name='assigned_time_list'),
    path('assignedtime/<int:id>/', AssignedTimeView.as_view(), name='assigned_time'),
    
]

# urlpatterns = format_suffix_patterns(urlpatterns)
