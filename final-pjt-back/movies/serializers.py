from rest_framework import serializers
from .models import Actor, Genre, Movie
from accounts.serializers import UserSerializer
from tastingrooms.serializers import TastingroomListSerializer
from baskets.serializers import BasketListSerializer


# MovieSerializer
    # poster_path, title, runtime, origin_country, vote_average, release_date, actors, genres, overview
    # 테이스팅룸: tastingroom_name, tastingroom_participants 사람수
    # 바스켓: (역참조) img, title
class MovieDetailSerializer(serializers.ModelSerializer):

    class ActorListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'

    class GenreListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    actors = ActorListSerializer(many=True)
    genres = GenreListSerializer(many=True)
    movie_tastingrooms = TastingroomListSerializer(many=True)
    movies_baskets = BasketListSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            'id', 'poster_path', 'title', 'runtime', 'origin_country', 'vote_average', 'release_date',
            'actors', 'genres', 'overview', 'movie_tastingrooms', 'movies_baskets',
            )
        read_only_fields = ('actors', 'genres', 'movie_tastingrooms', 'movies_baskets',)
    


# poster_path, title, release_date, vote_average
class MovieListSerializer(serializers.ModelSerializer):

    like_users = UserSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('title', 'release_date', 'poster_path', 'like_users',)
        read_only_fields = ('like_users',)