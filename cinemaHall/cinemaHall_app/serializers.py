from django_filters import NumberFilter
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    reservation = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                      view_name='reservation-detail')

    class Meta:
        model = User
        fields = ['id_user', 'user_name', 'password', 'email', 'age', 'reservation']


class TicketOptionsSerializer(serializers.HyperlinkedModelSerializer):
    reservation = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                      view_name='reservation-detail')

    class Meta:
        model = Ticket_options
        fields = ['id_ticket', 'name_ticket', 'price', 'number_of_seats', 'reservation']


class PegiSerializer(serializers.HyperlinkedModelSerializer):
    films = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='film-detail')

    class Meta:
        model = Pegi
        fields = ['id_pegi', 'age_range', 'films']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    films = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='film-detail')

    class Meta:
        model = Category
        fields = ['id_category', 'name', 'films']


class TransalationSerializer(serializers.HyperlinkedModelSerializer):
    filmshows = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                    view_name='filmshows-detail')

    class Meta:
        model = Transalation
        fields = ['id_translation', 'name_translation', 'filmshows']


class CinemaHallSerializer(serializers.HyperlinkedModelSerializer):
    filmshows = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                    view_name='filmshows-detail')
    seats = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                view_name='seats-detail')

    class Meta:
        model = Cinema_hall
        fields = ['id', 'size', 'use_3d', 'filmshows', 'seats']


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    id_category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    id_pegi = serializers.SlugRelatedField(queryset=Pegi.objects.all(), slug_field='age_range')
    filmshows = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                    view_name='filmshows-detail')

    class Meta:
        model = Film
        fields = ['id_film', 'id_category', 'id_pegi', 'title', 'filmshows']


class SeatsSerializer(serializers.HyperlinkedModelSerializer):
    id_cinema_hall = serializers.SlugRelatedField(queryset=Cinema_hall.objects.all(), slug_field='size')
    reservation = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                      view_name='reservation-detail')

    class Meta:
        model = Seats
        fields = ['id_seat', 'id_cinema_hall', 'x', 'y', 'its_fill', 'reservation']


class FilmShowsSerializer(serializers.HyperlinkedModelSerializer):
    id_film = serializers.SlugRelatedField(queryset=Film.objects.all(), slug_field='title')
    id_CinemaHall = serializers.SlugRelatedField(queryset=Cinema_hall.objects.all(), slug_field='size')
    id_Translation = serializers.SlugRelatedField(queryset=Transalation.objects.all(),
                                                  slug_field='name_translation')

    class Meta:
        model = Film_shows
        fields = ['id_film_shows', 'id_film', 'id_CinemaHall', 'id_Translation', 'date']


class GiveMeSeatSerializer(serializers.HyperlinkedModelSerializer):
    id_seat = serializers.SlugRelatedField(queryset=Seats.objects.all(), slug_field='its_fill')
    id_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='user_name')
    id_ticket_options = serializers.SlugRelatedField(queryset=Ticket_options.objects.all(), slug_field='name_ticket')

    class Meta:
        model = Give_me_seat
        fields = ['id_give_me_seat', 'id_seat', 'id_ticket_options', 'id_user']
