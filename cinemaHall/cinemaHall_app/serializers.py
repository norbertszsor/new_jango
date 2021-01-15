from rest_framework import serializers
from .models import *
from datetime import datetime


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id_user', 'user_name', 'password', 'email', 'age']


class TicketOptionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket_options
        fields = ['id_ticket', 'name_ticket', 'price', 'number_of_seats']


class PegiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pegi
        fields = ['id_pegi', 'age_range']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id_category', 'name']


class TransalationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transalation
        fields = ['id_translation', 'name_translation']


class CinemaHallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema_hall
        fields = ['id', 'size', 'use_3d']


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    id_category = serializers.SlugRelatedField(queryset=Category.objects.all(),slug_field='name')
    id_pegi = serializers.SlugRelatedField(queryset=Pegi.objects.all(),slug_field='age_range')

    class Meta:
        model = Film
        fields = ['id_film', 'id_category', 'id_pegi', 'title']


class SeatsSerializer(serializers.HyperlinkedModelSerializer):
    id_cinema_hall = serializers.SlugRelatedField(queryset=Cinema_hall.objects.all(),slug_field='size')
    class Meta:
        model = Seats
        fields = ['id_seat', 'id_cinema_hall', 'x', 'y', 'its_fill']


class FilmShowsSerializer(serializers.HyperlinkedModelSerializer):
    id_film = serializers.SlugRelatedField(queryset=Film.objects.all(),slug_field='title')
    id_CinemaHall = serializers.SlugRelatedField(queryset=Cinema_hall.objects.all(),slug_field='size')
    id_Translation = serializers.SlugRelatedField(queryset=Transalation.objects.all(),
                                                  slug_field='name_translation')
    class Meta:
        model = Film_shows
        fields = ['id_film_shows', 'id_film', 'id_CinemaHall', 'id_Translation', 'date']


class GiveMeSeatSerializer(serializers.HyperlinkedModelSerializer):
    id_seat = serializers.SlugRelatedField(queryset=Seats.objects.all(),slug_field='its_fill')
    id_user = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='user_name')
    id_ticket_options = serializers.SlugRelatedField(queryset=Ticket_options.objects.all(),slug_field='name_ticket')
    class Meta:
        model = Give_me_seat
        fields = ['id_give_me_seat', 'id_seat', 'id_ticket_options', 'id_user']
