from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import generics
from .serializers import *
from . import views

urlpatterns = [
    path('', views.homePage, name ='index'),
    path(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('TEST/', views.product_list),

    path('users/', views.UserList.as_view()),
    path('users/<int:id>/', views.UserDetail.as_view()),
    path('users/create', views.UserCreate.as_view()),
    path('users/create/<int:pk>/', views.UserCreate.as_view()),

    path('tickets/', views.TicketOptionsList.as_view()),
    path('tickets/<int:pk>/', views.TicketOptionsDetail.as_view()),
    path('tickets/create', views.TicketOptionsCreate.as_view()),
    path('tickets/create/<int:pk>/', views.TicketOptionsCreate.as_view()),

    path('pegi/', views.PegiList.as_view()),
    path('pegi/<int:pk>/', views.PegiDetail.as_view()),
    path('pegi/create', views.PegiCreate.as_view()),
    path('pegi/create/<int:pk>/', views.PegiCreate.as_view()),

    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('category/create', views.CategoryCreate.as_view()),
    path('category/create/<int:pk>/', views.CategoryCreate.as_view()),

    path('translation/', views.TranslationList.as_view()),
    path('translation/<int:pk>/', views.TranslationDetail.as_view()),
    path('translation/create', views.TranslationCreate.as_view()),
    path('translation/create/<int:pk>/', views.TranslationCreate.as_view()),

    path('cinemahall/', views.CinemaHallList.as_view()),
    path('cinemahall/<int:pk>/', views.CinemaHallLDetail.as_view()),
    path('cinemahall/create', views.CinemaHallCreate.as_view()),
    path('cinemahall/create/<int:pk>/', views.CinemaHallCreate.as_view()),

    path('film/', views.FilmList.as_view()),
    path('film/<int:pk>/', views.FilmDetail.as_view()),
    path('film/create', views.FilmCreate.as_view()),
    path('film/create/<int:pk>/', views.FilmCreate.as_view()),

    path('seats/', views.SeatsList.as_view()),
    path('seats/<int:pk>/', views.SeatsDetail.as_view()),
    path('seats/create', views.SeatsCreate.as_view()),
    path('seats/create/<int:pk>/', views.SeatsCreate.as_view()),

    path('filmshows/', views.FilmShowsList.as_view()),
    path('filmshows/<int:pk>/', views.FilmShowsDetail.as_view()),
    path('filmshows/create', views.FilmShowsCreate.as_view()),
    path('filmshows/create/<int:pk>/', views.FilmShowsCreate.as_view()),

    path('givemeseats/', views.GiveMeSeatList.as_view()),
    path('givemeseats/<int:pk>/', views.GiveMeSeatDetail.as_view()),
    path('givemeseats/create', views.GiveMeSeatCreate.as_view()),
    path('givemeseats/create/<int:pk>/', views.GiveMeSeatCreate.as_view()),
]