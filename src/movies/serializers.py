from rest_framework import serializers
from imdbpie import Imdb

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    created_date = serializers.CharField(max_length=200, read_only=True)
    modified_date = serializers.CharField(max_length=200, read_only=True)
    imdb_id = serializers.CharField(max_length=200, allow_blank=True)
    year = serializers.CharField(max_length=200, allow_blank=True)

    class Meta:
        model = Movie
        fields = ('name', 'created_date', 'modified_date', 'imdb_id', 'year')

    def create(self, validated_data):

        imdb = Imdb()
        movies = imdb.search_for_title(validated_data['name'])
        if movies:
            movie_name = movies[0]['title']
            imdb_id = movies[0]['imdb_id']
            year = movies[0]['year']
            validated_data['name'] = movie_name
            validated_data['imdb_id'] = imdb_id
            validated_data['year'] = year

            return super(MovieSerializer, self).create(validated_data)

