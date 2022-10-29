from django.urls import path
from accounts import views 
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/', views.LoadUserView.as_view(), name='load_user'),
    path('user/<int:user_id>/group/', views.UserGroupView.as_view(), name= "user_group_assign")
]