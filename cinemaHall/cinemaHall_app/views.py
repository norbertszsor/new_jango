from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework import generics, permissions
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
            'UserCinema': reverse(UserCinemaList.name, request=request),
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


class UserCinemaList(generics.ListCreateAPIView):
    queryset = UserCinema.objects.all()
    serializer_class = UserCinemaSerializer
    name = 'usercinema-list'
    filterset_fields = ['user_name', 'email', 'age']
    search_fields = ['user_name']
    ordering_fields = ['id_user', 'user_name', 'age']
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(ownerUser=self.request.user)


class UserCinemaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCinema.objects.all()
    serializer_class = UserCinemaSerializer
    name = 'usercinema-detail'
    permission_classes = [permissions.IsAdminUser]


class TicketList(generics.ListCreateAPIView):
    queryset = Ticket_options.objects.all()
    serializer_class = TicketOptionsSerializer
    name = 'ticket-list'
    filterset_fields = ['name_ticket', 'reservation']
    search_fields = ['name_ticket']
    ordering_fields = ['name_ticket', 'price', 'reservation']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket_options.objects.all()
    serializer_class = TicketOptionsSerializer
    name = 'ticket-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PegiListFilter(FilterSet):
    minAge = NumberFilter(field_name='age_range', lookup_expr='gte')
    maxAge = NumberFilter(field_name='age_range', lookup_expr='lte')

    class meta:
        model = Pegi
        fields = ['minAge', 'maxAge']

class PegiList(generics.ListCreateAPIView):
    queryset = Pegi.objects.all()
    serializer_class = PegiSerializer
    name = 'pegi-list'
    filter_class = PegiListFilter
    ordering_fields = ['age_range']
    search_fields = ['age_range']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PegiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pegi.objects.all()
    serializer_class = PegiSerializer
    name = 'pegi-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(ownerCategory=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TransalationList(generics.ListCreateAPIView):
    queryset = Transalation.objects.all()
    serializer_class = TransalationSerializer
    name = 'transalation-list'
    filterset_fields = ['name_translation']
    ordering_fields = ['name_translation']
    search_fields = ['name_translation']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TransalationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transalation.objects.all()
    serializer_class = TransalationSerializer
    name = 'translation-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CinemaHallList(generics.ListCreateAPIView):
    queryset = Cinema_hall.objects.all()
    serializer_class = CinemaHallSerializer
    name = 'cinemahall-list'
    permission_classes = [permissions.IsAuthenticated]


class CinemaHallDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema_hall.objects.all()
    serializer_class = CinemaHallSerializer
    name = 'cinemahall-detail'
    permission_classes = [permissions.IsAuthenticated]


class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = 'film-list'
    filterset_fields = ['id_film', 'id_category', 'id_pegi']
    search_fields = ['title']
    ordering_fields = ['id_film']
    permission_classes = [permissions.IsAuthenticated]


class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = 'film-detail'
    permission_classes = [permissions.IsAuthenticated]


class SeatsList(generics.ListCreateAPIView):
    minAge = NumberFilter(field_name='age_range', lookup_expr='gte')
    maxAge = NumberFilter(field_name='age_range', lookup_expr='lte')
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    name = 'seats-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SeatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    name = 'seats-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FilmShowsListFilter(FilterSet):
    fromDate = DateTimeFilter(field_name='date', lookup_expr='gte')
    toDate = DateTimeFilter(field_name='date', lookup_expr='lte')

    class meta:
        model = Film_shows
        fields = ['fromDate', 'toDate']


class FilmShowsList(generics.ListCreateAPIView):
    queryset = Film_shows.objects.all()
    serializer_class = FilmShowsSerializer
    name = 'filmshows-list'
    filter_class = FilmShowsListFilter
    ordering_fields = ['id_film_shows', 'id_film', 'id_CinemaHall']
    search_fields = ['id_film', 'id_CinemaHall']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FilmShowsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film_shows.objects.all()
    serializer_class = FilmShowsSerializer
    name = 'filmshows-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GiveMeSeatList(generics.ListCreateAPIView):
    queryset = Give_me_seat.objects.all()
    serializer_class = GiveMeSeatSerializer
    name = 'reservation-list'
    permission_classes = [permissions.IsAuthenticated]


class GiveMeSeatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Give_me_seat.objects.all()
    serializer_class = GiveMeSeatSerializer
    name = 'reservation-detail'
    permission_classes = [permissions.IsAuthenticated]
