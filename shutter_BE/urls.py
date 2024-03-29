"""shutter_BE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from studio.views import TownView

urlpatterns = [
    path('studio/', include('studio.urls')),
    path('admin/', admin.site.urls),
    path('photo/', include('photo.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path("reservation/", include("reservation.urls")),
    path('town/', TownView.as_view(), name="all_town"),
    path('tags/', include('tags.urls'))
]
