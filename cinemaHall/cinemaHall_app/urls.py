from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]