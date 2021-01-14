from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import *
from .models import *


def homepage(request):
    return HttpResponse('HomePage')


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


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
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'pegi-detail'


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'


class TranslationList(generics.ListCreateAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    name = 'translation-list'


class TranslationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
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
