from django.shortcuts import get_object_or_404, render
from pprint import pprint

# REST framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# model
from .models import Movie, Genre, Actor

# serializer
from .serializers import MovieDetailSerializer, MovieListSerializer

# orm
from django.db.models import Q

# api
from decouple import config
from rest_framework.decorators import api_view
import requests

# login user
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



# movie search (index, 영화섹션용) (검색어 필터링해서 다 보여주는거) 영화명, 배우, 장르 (평점순)
@api_view(['GET'])
def movies_search(request, query):
    movies = Movie.objects.filter(
        Q(title__icontains=query)|
        Q(actors__name__icontains=query)|
        Q(genres__name__icontains=query)
        ).distinct().order_by('-vote_average')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# movie detail
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)
    

# [TMDB API 받아오기]
# 영화
@api_view(['POST'])
def tmdb_movies(request):
    TMDB_API_KEY = config("TMDB_API_KEY")
    for page in range(1, 2):
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko&page={page}'
        request = requests.get(url).json()
        for result in request.get('results'):
            movie_id = str(result.get('id'))
            # genre, origin_country, runtime
            detail_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=ko'
            detail_result = requests.get(detail_url).json()
            # actors
            credit_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko'
            credit_result = requests.get(credit_url).json()
            movie = Movie.objects.create(
                title = result.get('title'),
                overview = result.get('overview'),
                poster_path = result.get('poster_path'),
                vote_average = result.get('vote_average'),
                release_date = result.get('release_date'),
                adult = result.get('adult'),
                runtime = detail_result.get('runtime'),
            )
            # 장르 처리
            for genre_name in detail_result.get('genres'):
                if Genre.objects.filter(name=genre_name.get('name')).exists():
                    genre = get_object_or_404(Genre, name=genre_name.get('name'))
                else:
                    genre = Genre.objects.create(name=genre_name.get('name'))
                # genre = Genre.objects.get(name=genre_name.get('name')) ### create로 하면 중복데이터 저장됨
                genre.movies.add(movie)
            # 배우 처리
            for cast in credit_result.get('cast'):
                if cast.get('known_for_department') == 'Acting':
                    if Actor.objects.filter(name=cast.get('name')).exists():
                        actor = get_object_or_404(Actor, name=cast.get('name'))
                    else:
                        actor = Actor.objects.create(name=cast.get('name'))
                    movie.actors.add(actor)
    return Response({ 'db': '가져왔습니다.' })




# 나중에~~~
# genre(전체 아마 19개인듯) 나중에
# actor(랜덤으로 20개) 나중에