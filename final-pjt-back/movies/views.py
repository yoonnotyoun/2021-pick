from django.shortcuts import render

# api 관련
from decouple import config
from rest_framework.decorators import api_view
import requests



# movie search (index, 영화섹션용) (검색어 필터링해서 다 보여주는거)


# movie detail
    

# [TMDB API 받아오기]
# 영화
def db_movies(request):
    TMDB_API_KEY = config("TMDB_API_KEY")
    for page in range(1, 2):
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko&page={page}'
        request = requests.get(url).json()
        print(request)


# 장르
def db_genres(request):
    TMDB_API_KEY = config("TMDB_API_KEY")
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko&page={page}'
    request = requests.get(url).json()
    print(request)


# 배우
def db_actors(request):
    TMDB_API_KEY = config("TMDB_API_KEY")
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko&page={page}'
    request = requests.get(url).json()
    print(request)


# 나중에~~~
# genre(전체 아마 19개인듯) 나중에
# actor(랜덤으로 20개) 나중에