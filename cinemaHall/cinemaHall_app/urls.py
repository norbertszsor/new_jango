from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name ='index'),
    path(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('tickets/', views.TicketOptionsList.as_view()),
    path('tickets/<int:pk>/', views.TicketOptionsDetail.as_view()),
    path('pegi/', views.PegiList.as_view()),
    path('pegi/<int:pk>/', views.PegiDetail.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('translation/', views.TranslationList.as_view()),
    path('translation/<int:pk>/', views.TranslationDetail.as_view()),
    path('cinemahall/', views.CinemaHallList.as_view()),
    path('cinemahall/<int:pk>/', views.CinemaHallLDetail.as_view()),
    path('film/', views.FilmList.as_view()),
    path('film/<int:pk>/', views.FilmDetail.as_view()),
    path('seats/', views.SeatList.as_view()),
    path('seats/<int:pk>/', views.SeatDetail.as_view()),
    path('filmshows/', views.FilmShowsList.as_view()),
    path('filmshows/<int:pk>/', views.FilmShowsDetail.as_view()),
    path('givemeseats/', views.GiveMeSeatList.as_view()),
    path('givemeseats/<int:pk>/', views.GiveMeSeatDetail.as_view()),
]