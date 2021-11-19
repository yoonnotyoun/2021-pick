from django.shortcuts import render
from pprint import pprint

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# model
from .models import Movie, Genre, Actor

# api
from decouple import config
from rest_framework.decorators import api_view
import requests

# login user
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



# movie search (index, 영화섹션용) (검색어 필터링해서 다 보여주는거)


# movie detail
    

# [TMDB API 받아오기]
# 장르
@api_view(['POST'])
def db_genres(request):
    TMDB_API_KEY = config("TMDB_API_KEY")
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&region=KR&language=ko'
    request = requests.get(url).json()
    for genre in request.get('genres'):
        Genre.objects.create(name=genre.get('name'))

    return Response({ 'db': '가져왔습니다.' })

# 배우
# @api_view(['POST'])
# def db_actors(request):
#     TMDB_API_KEY = config("TMDB_API_KEY")
#     url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko&page={page}'
#     request = requests.get(url).json()
#     print(request)

# 영화
@api_view(['POST'])
def db_movies(request):
    TMDB_API_KEY = config("TMDB_API_KEY")
    for page in range(1, 2):
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko&page={page}'
        request = requests.get(url).json()
        # pprint(requests.get(url).json())
        for result in request.get('results'):
            # pprint(result)
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
            # pprint(credit_result.get('cast'))
            # 장르 처리
            for genre_name in detail_result.get('genres'):
                if Genre.objects.filter(name=genre_name.get('name')).exists():
                    genre = Genre.objects.get(name=genre_name.get('name'))
                else:
                    genre = Genre.objects.create(name=genre_name.get('name'))
                # genre = Genre.objects.get(name=genre_name.get('name')) ### create로 하면 중복데이터 저장됨
                genre.movies.add(movie)
            # 배우 처리
            for cast_name in credit_result.get('cast'):
                if Actor.objects.filter(name=cast_name.get('name')).exists():
                    actor = Actor.objects.get(name=cast_name.get('name'))
                else:
                    actor = Actor.objects.create(name=cast_name.get('name'))
                movie.actors.add(actor)
    return Response({ 'db': '가져왔습니다.' })




# 나중에~~~
# genre(전체 아마 19개인듯) 나중에
# actor(랜덤으로 20개) 나중에