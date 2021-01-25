from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AdminMenu.as_view(), name=views.AdminMenu.name),

    path('user-list', views.UserList.as_view(), name=views.UserList.name),
    path('user-detail/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),

    path('ticket-list', views.TicketList.as_view(), name=views.TicketList.name),
    path('ticket-detail/<int:pk>', views.TicketDetail.as_view(),name=views.TicketDetail.name),

    path('pegi-list', views.PegiList.as_view(), name=views.PegiList.name),
    path('pegi-detail/<int:pk>', views.PegiDetail.as_view(), name=views.PegiDetail.name),

    path('category-list', views.CategoryList.as_view(), name=views.CategoryList.name),
    path('category-detail/<int:pk>', views.CategoryDetail.as_view(), name=views.CategoryDetail.name),

    path('transalation-list', views.TransalationList.as_view(), name=views.TransalationList.name),
    path('transalation-detail/<int:pk>', views.TransalationDetail.as_view(),name=views.TransalationDetail.name),

    path('cinemahall-list', views.CinemaHallList.as_view(), name=views.CinemaHallList.name),
    path('cinemahall-detail/<int:pk>', views.CinemaHallDetail.as_view(),name=views.CinemaHallDetail.name),

    path('film-list', views.FilmList.as_view(), name=views.FilmList.name),
    path('film-detail/<int:pk>', views.FilmDetail.as_view(), name=views.FilmDetail.name),

    path('seats-list', views.SeatsList.as_view(), name=views.SeatsList.name),
    path('seats-detail/<int:pk>', views.SeatsDetail.as_view(),name=views.SeatsDetail.name),

    path('filmshows-list', views.FilmShowsList.as_view(), name=views.FilmShowsList.name),
    path('filmshows-detail/<int:pk>', views.FilmShowsDetail.as_view(), name=views.FilmShowsDetail.name),

    path('reservation-list', views.GiveMeSeatList.as_view(), name=views.GiveMeSeatList.name),
    path('reservation-detail/<int:pk>', views.GiveMeSeatDetail.as_view(), name=views.GiveMeSeatDetail.name),


]