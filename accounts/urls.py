from django.urls import path
from accounts import views,socialviews
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/', views.LoadUserView.as_view(), name='load_user'),
    path('user/<int:user_id>/group/', views.UserGroupView.as_view(), name= "user_group_assign"),

    path('kakao/login/', socialviews.kakao_login, name='kakao_login'),
    path('kakao/login/callback/', socialviews.kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', socialviews.KakaoLoginView.as_view(), name='kakao_login_todjango'),

]