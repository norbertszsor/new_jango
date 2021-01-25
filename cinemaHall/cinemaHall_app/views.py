from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
import django_filters.rest_framework
from rest_framework.reverse import reverse
from .serializers import *
from .models import *


class AdminMenu(generics.GenericAPIView):
    name = 'Admin-Menu'

    def get(self, request):
        return Response({
            'User': reverse(UserList.name, request=request),
            'Tickets': reverse(TicketList.name, request=request),
            'Pegi': reverse(PegiList.name, request=request),
            'Category': reverse(CategoryList.name, request=request),
            'Translation': reverse(TransalationList.name, request=request),
            'CinemaHall': reverse(CinemaHallList.name, request=request),
            'Film': reverse(FilmList.name, request=request),
            'Seats': reverse(SeatsList.name, request=request),
            'FilmShows': reverse(FilmShowsList.name, request=request),
            'Reservation': reverse(GiveMeSeatList.name, request=request),

        })


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    filter_fields = ['user_name', 'email', 'age']
    search_fields = ['id_user', 'user_name']
    ordering_fields = ['id_user', 'user_name', 'email', 'age']


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class TicketList(generics.ListCreateAPIView):
    queryset = Ticket_options.objects.all()
    serializer_class = TicketOptionsSerializer
    name = 'ticket-list'


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket_options.objects.all()
    serializer_class = TicketOptionsSerializer
    name = 'ticket-detail'


class PegiList(generics.ListCreateAPIView):
    queryset = Pegi.objects.all()
    serializer_class = PegiSerializer
    name = 'pegi-list'


class PegiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pegi.objects.all()
    serializer_class = PegiSerializer
    name = 'pegi-detail'


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'


class TransalationList(generics.ListCreateAPIView):
    queryset = Transalation.objects.all()
    serializer_class = TransalationSerializer
    name = 'transalation-list'


class TransalationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transalation.objects.all()
    serializer_class = TransalationSerializer
    name = 'translation-detail'


class CinemaHallList(generics.ListCreateAPIView):
    queryset = Cinema_hall.objects.all()
    serializer_class = CinemaHallSerializer
    name = 'cinemahall-list'


class CinemaHallDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema_hall.objects.all()
    serializer_class = CinemaHallSerializer
    name = 'cinemahall-detail'


class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = 'film-list'


class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = 'film-detail'


class SeatsList(generics.ListCreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    name = 'seats-list'


class SeatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    name = 'seats-detail'


class FilmShowsList(generics.ListCreateAPIView):
    queryset = Film_shows.objects.all()
    serializer_class = FilmShowsSerializer
    name = 'filmshows-list'


class FilmShowsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film_shows.objects.all()
    serializer_class = FilmShowsSerializer
    name = 'filmshows-detail'


class GiveMeSeatList(generics.ListCreateAPIView):
    queryset = Give_me_seat.objects.all()
    serializer_class = GiveMeSeatSerializer
    name = 'reservation-list'


class GiveMeSeatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Give_me_seat.objects.all()
    serializer_class = GiveMeSeatSerializer
    name = 'reservation-detail'
