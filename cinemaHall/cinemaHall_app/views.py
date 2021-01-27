from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework import generics, mixins
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import *
from .filters import *

def homePage(request):
    return HttpResponse('HomePage')

# ------------------------------USER

def product_list(request):
    f = UserFilter(request.GET, queryset=User.objects.all())
    return render(request, 'templates/form.html', {'filter': f})

class UserList(APIView):

    def get(self, request, format=None):
        modele = User.objects.all()
        serializer_class = UserSerializer(modele, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = UserSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = UserFilter(self.request.GET, querysetset = self.get_queryset())

class UserDetail(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = UserSerializer(modele)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = UserSerializer(modele, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modele = self.get_object(pk)
        modele.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserCreate(generics.ListCreateAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    filter_fields = ['user_name', 'password']
    search_fields = ['user_name']
    ordering_fields = ['user_name']

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk = None):
        return self.update(request, pk)

    def delete(self, request, pk = None):
        return self.destroy(request, pk)

# ------------------------------TICKET_OPTIONS
class TicketOptionsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get(self, request, format=None):
        modele = Ticket_options.objects.all()
        serializer_class = TicketOptionsSerializer(modele, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = TicketOptionsSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketOptionsDetail(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get_object(self, pk):
        try:
            return Ticket_options.objects.get(pk=pk)
        except Ticket_options.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = TicketOptionsSerializer(modele)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = TicketOptionsSerializer(modele, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modele = self.get_object(pk)
        modele.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketOptionsCreate(generics.ListCreateAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Ticket_options.objects.all()
    serializer_class = TicketOptionsSerializer
    lookup_field = 'pk'


    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk = None):
        return self.update(request, pk)

    def delete(self, request, pk = None):
        return self.destroy(request, pk)

# ------------------------------Pegi
class PegiList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get(self, request, format=None):
        modele = Pegi.objects.all()
        serializer_class = PegiSerializer(modele, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = PegiSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class PegiDetail(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get_object(self, pk):
        try:
            return Pegi.objects.get(pk=pk)
        except Pegi.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = PegiSerializer(modele)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = PegiSerializer(modele, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modele = self.get_object(pk)
        modele.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PegiCreate(generics.ListCreateAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Pegi.objects.all()
    serializer_class = PegiSerializer
    lookup_field = 'pk'


    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk = None):
        return self.update(request, pk)

    def delete(self, request, pk = None):
        return self.destroy(request, pk)


# ------------------------------Category
class CategoryList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get(self, request, format=None):
        modele = Category.objects.all()
        serializer_class = CategorySerializer(modele, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = CategorySerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = CategorySerializer(modele)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = CategorySerializer(modele, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modele = self.get_object(pk)
        modele.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryCreate(generics.ListCreateAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk = None):
        return self.update(request, pk)

    def delete(self, request, pk = None):
        return self.destroy(request, pk)

# ------------------------------Translation
class TranslationList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get(self, request, format=None):
        modele = Translation.objects.all()
        serializer_class = TranslationSerializer(modele, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = TranslationSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class TranslationDetail(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get_object(self, pk):
        try:
            return Translation.objects.get(pk=pk)
        except Translation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = TranslationSerializer(modele)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = TranslationSerializer(modele, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modele = self.get_object(pk)
        modele.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TranslationCreate(generics.ListCreateAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    lookup_field = 'pk'


    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk = None):
        return self.update(request, pk)

    def delete(self, request, pk = None):
        return self.destroy(request, pk)

# ------------------------------Cinema_hall
class CinemaHallList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get(self, request, format=None):
        modele = Cinema_hall.objects.all()
        serializer_class = CinemaHallSerializer(modele, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = CinemaHallSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class CinemaHallLDetail(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get_object(self, pk):
        try:
            return Cinema_hall.objects.get(pk=pk)
        except Cinema_hall.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = CinemaHallSerializer(modele)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = CinemaHallSerializer(modele, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modele = self.get_object(pk)
        modele.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CinemaHallCreate(generics.ListCreateAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Cinema_hall.objects.all()
    serializer_class = CinemaHallSerializer
    lookup_field = 'pk'


    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk = None):
        return self.update(request, pk)

    def delete(self, request, pk = None):
        return self.destroy(request, pk)

# ------------------------------Film
class FilmList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get(self, request, format=None):
        modele = Film.objects.all()
        serializer_class = FilmSerializer(modele, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = FilmSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class FilmDetail(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get_object(self, pk):
        try:
            return Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = FilmSerializer(modele)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = FilmSerializer(modele, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modele = self.get_object(pk)
        modele.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FilmCreate(generics.ListCreateAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    lookup_field = 'pk'


    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk = None):
        return self.update(request, pk)

    def delete(self, request, pk = None):
        return self.destroy(request, pk)

# ------------------------------Seats
class SeatsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get(self, request, format=None):
        modele = Seats.objects.all()
        serializer_class = SeatsSerializer(modele, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = SeatsSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class SeatsDetail(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get_object(self, pk):
        try:
            return Seats.objects.get(pk=pk)
        except Seats.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = SeatsSerializer(modele)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = SeatsSerializer(modele, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modele = self.get_object(pk)
        modele.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SeatsCreate(generics.ListCreateAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    lookup_field = 'pk'


    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk = None):
        return self.update(request, pk)

    def delete(self, request, pk = None):
        return self.destroy(request, pk)

# ------------------------------Film_shows
class FilmShowsList(APIView):

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get(self, request, format=None):
        modele = Film_shows.objects.all()
        serializer_class = FilmShowsSerializer(modele, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = FilmShowsSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class FilmShowsDetail(APIView):

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get_object(self, pk):
        try:
            return Film_shows.objects.get(pk=pk)
        except Film_shows.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = FilmShowsSerializer(modele)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = FilmShowsSerializer(modele, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modele = self.get_object(pk)
        modele.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FilmShowsCreate(generics.ListCreateAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Film_shows.objects.all()
    serializer_class = FilmShowsSerializer
    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk = None):
        return self.update(request, pk)

    def delete(self, request, pk = None):
        return self.destroy(request, pk)

# ------------------------------Give_me_seat
class GiveMeSeatList(APIView):

    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get(self, request, format=None):
        modele = Give_me_seat.objects.all()
        serializer_class = GiveMeSeatSerializer(modele, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = GiveMeSeatSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class GiveMeSeatDetail(APIView):


    def get(self, request, format=None):
        content = {
            'status': 'Musisz być zalogowany'
        }
        return Response(content)

    def get_object(self, pk):
        try:
            return Give_me_seat.objects.get(pk=pk)
        except Give_me_seat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = GiveMeSeatSerializer(modele)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer_class = GiveMeSeatSerializer(modele, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modele = self.get_object(pk)
        modele.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GiveMeSeatCreate(generics.ListCreateAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    permission_classes = [IsAdminUser]
    queryset = Give_me_seat.objects.all()
    serializer_class = GiveMeSeatSerializer
    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk = None):
        return self.update(request, pk)

    def delete(self, request, pk = None):
        return self.destroy(request, pk)