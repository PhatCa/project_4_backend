from django.shortcuts import render
from rest_framework import generics
from .serializers import MovieSerializer
from .models import Movie
# Create your views here.

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer
