from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from movies.models import Movie
from movies.serializers import MovieSerializer


class MoviesViewSet(viewsets.ViewSet, ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
