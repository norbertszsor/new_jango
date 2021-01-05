from rest_framework import serializers
from .models import *
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_user', 'user_name', 'password', 'email', 'age']

class TicketOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket_options
        fields = ['id_ticket', 'name_ticket', 'price', 'number_of_seats', 'age']

class PegiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pegi
        fields = ['id_pegi', 'age_range']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id_category', 'name']

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transalation
        fields = ['id_translation', 'name_translation']

class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema_hall
        fields = ['id', 'size', 'use_3d']

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id_film','id_category', 'id_pegi', 'title']
    def validate_date(self, value):
        if (value < datetime.now()):
            raise serializers.ValidationError("Invalid date")
        return value

class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = ['id_seat', 'id_cinema_hall', 'x', 'y', 'its_fill']

class FilmShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film_shows
        fields = ['id_film_shows', 'id_film', 'id_CinemaHall', 'id_Translation', 'date']

class GiveMeSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Give_me_seat
        fields = ['id_give_me_seat', 'id_seat', 'id_ticket_options', 'id_user']