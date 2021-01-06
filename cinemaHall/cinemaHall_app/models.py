from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=45)
    age = models.IntegerField(null=False)

class Ticket_options(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    name_ticket = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    number_of_seats = models.IntegerField()

class Pegi(models.Model):
    id_pegi = models.AutoField(primary_key = True)
    age_range = models.IntegerField()

class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

class Translation(models.Model):
    id_translation = models.AutoField(primary_key=True)
    name_translation = models.CharField(max_length=45)

class Cinema_hall(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.IntegerField()
    use_3d = models.SmallIntegerField()

class Film(models.Model):
    id_film = models.AutoField(primary_key=True)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id_pegi = models.ForeignKey(Pegi, on_delete=models.CASCADE)
    title = models.CharField(max_length=45)

class Seats(models.Model):
    id_seat = models.AutoField(primary_key=True)
    id_cinema_hall = models.ForeignKey(Cinema_hall, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    its_fill = models.SmallIntegerField()

class Film_shows(models.Model):
    id_film_shows = models.AutoField(primary_key=True)
    id_film = models.ForeignKey(Film, on_delete=models.CASCADE)
    id_CinemaHall = models.ForeignKey(Cinema_hall, on_delete=models.CASCADE)
    id_Translation = models.ForeignKey(Translation, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Give_me_seat(models.Model):
    id_give_me_seat = models.AutoField(primary_key=True)
    id_seat = models.ForeignKey(Seats, on_delete=models.CASCADE)
    id_ticket_options = models.ForeignKey(Ticket_options, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
