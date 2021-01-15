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

    path('ticket-list', views.TicketList.as_view()),
    path('ticket-detail/<int:pk>', views.TicketDetail.as_view()),

    path('pegi-list', views.PegiList.as_view()),
    path('pegi-detail/<int:pk>', views.PegiDetail.as_view()),

    path('category-list', views.CategoryList.as_view()),
    path('category-detail/<int:pk>', views.CategoryDetail.as_view()),

    path('transalation-list', views.TransalationList.as_view()),
    path('transalation-detail/<int:pk>', views.TransalationDetail.as_view()),

    path('cinemahall-list', views.CinemaHallList.as_view()),
    path('cinemahall-detail/<int:pk>', views.CinemaHallDetail.as_view()),

    path('film-list', views.FilmList.as_view()),
    path('film-detail/<int:pk>', views.FilmDetail.as_view()),

    path('seats-list', views.SeatsList.as_view()),
    path('seats-detail/<int:pk>', views.SeatsDetail.as_view()),

    path('filmshows-list', views.FilmShowsList.as_view()),
    path('filmshows-detail/<int:pk>', views.FilmShowsDetail.as_view()),

    path('reservation-list', views.GiveMeSeatList.as_view()),
    path('reservation-detail/<int:pk>', views.GiveMeSeatDetail.as_view()),


]