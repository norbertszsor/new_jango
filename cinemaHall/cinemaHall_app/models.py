from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class UserCinema(BaseModel):
    id_user = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=45)
    age = models.IntegerField(null=False)
    ownerUser = models.ForeignKey('auth.User', related_name='UserCinema', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.id_user)


class Ticket_options(BaseModel):
    id_ticket = models.AutoField(primary_key=True)
    name_ticket = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    number_of_seats = models.IntegerField()

    def __str__(self):
        return str(self.id_ticket)


class Pegi(BaseModel):
    id_pegi = models.AutoField(primary_key=True)
    age_range = models.IntegerField()

    def __str__(self):
        return str(self.id_pegi)


class Category(BaseModel):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    ownerCategory = models.ForeignKey('auth.User', related_name='UserCategory', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.id_category)



class Transalation(BaseModel):
    id_translation = models.AutoField(primary_key=True)
    name_translation = models.CharField(max_length=45)

    def __str__(self):
        return str(self.id_translation)


class Cinema_hall(BaseModel):
    id = models.AutoField(primary_key=True)
    size = models.IntegerField()
    use_3d = models.SmallIntegerField()

    def __str__(self):
        return str(self.id)


class Film(BaseModel):
    id_film = models.AutoField(primary_key=True)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='films')
    id_pegi = models.ForeignKey(Pegi, on_delete=models.CASCADE, related_name='films')
    title = models.CharField(max_length=45)

    def __str__(self):
        return str(self.id_film)


class Seats(BaseModel):
    id_seat = models.AutoField(primary_key=True)
    id_cinema_hall = models.ForeignKey(Cinema_hall, on_delete=models.CASCADE, related_name='seats')
    x = models.IntegerField()
    y = models.IntegerField()
    its_fill = models.SmallIntegerField()

    def __str__(self):
        return str(self.id_seat)


class Film_shows(BaseModel):
    id_film_shows = models.AutoField(primary_key=True)
    id_film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='filmshows')
    id_CinemaHall = models.ForeignKey(Cinema_hall, on_delete=models.CASCADE, related_name='filmshows')
    id_Translation = models.ForeignKey(Transalation, on_delete=models.CASCADE, related_name='filmshows')
    date = models.DateTimeField()

    def __str__(self):
        return str(self.id_film_shows)


class Give_me_seat(BaseModel):
    id_give_me_seat = models.AutoField(primary_key=True)
    id_seat = models.ForeignKey(Seats, on_delete=models.CASCADE, related_name='reservation')
    id_ticket_options = models.ForeignKey(Ticket_options, on_delete=models.CASCADE, related_name='reservation')
    id_user = models.ForeignKey(UserCinema, on_delete=models.CASCADE, related_name='reservation')

    def __str__(self):
        return self.id_give_me_seat
