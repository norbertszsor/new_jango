from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import generics
from .serializers import *
from . import views

urlpatterns = [
    path('', views.homepage, name ='index'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('user-list', views.UserList.as_view()),
    path('user-detail/<int:pk>', views.UserDetail.as_view()),

    path('ticket-list', views.UserList.as_view()),
    path('ticket-detail/<int:pk>', views.UserDetail.as_view()),

    path('pegi-list', views.UserList.as_view()),
    path('pegi-detail/<int:pk>', views.UserDetail.as_view()),

    path('category-list', views.UserList.as_view()),
    path('category-detail/<int:pk>', views.UserDetail.as_view()),

    path('translation-list', views.UserList.as_view()),
    path('translation-detail/<int:pk>', views.UserDetail.as_view()),

    path('cinemahall-list', views.UserList.as_view()),
    path('cinemahall-detail/<int:pk>', views.UserDetail.as_view()),

    path('film-list', views.UserList.as_view()),
    path('film-detail/<int:pk>', views.UserDetail.as_view()),

    path('seats-list', views.UserList.as_view()),
    path('seats-detail/<int:pk>', views.UserDetail.as_view()),

    path('filmshows-list', views.UserList.as_view()),
    path('filmshows-detail/<int:pk>', views.UserDetail.as_view()),

    path('reservation-list', views.UserList.as_view()),
    path('reservation-detail/<int:pk>', views.UserDetail.as_view()),


]