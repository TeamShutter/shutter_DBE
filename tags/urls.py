from django.urls import path
from .views import AllTagView

app_name= 'tags'
urlpatterns =[
    path('', AllTagView.as_view(), name="get_all_tag"),
    # path('<int:tag_id>/', TagView.as_view(), name="get single tag" ),
    # path('phototag/', PhotoTagView.as_view(), name='create photo tag')
]