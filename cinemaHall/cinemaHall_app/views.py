from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

def homePage(request):
    return HttpResponse('HomePage')

class userList(generics.ListCreateAPIView):
    queryset = User.user_name.all()
    serializer_class = UserSerializer

class userDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.user_name.all()
    serializer_class = UserSerializer



