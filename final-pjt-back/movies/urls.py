from django.urls import path
from . import views

urlpatterns = [
    # 영화 기본 기능
    path('search/<query>/', views.movies_search),
    path('<int:movie_pk>/', views.movie_detail),

    # tmdb api
    path('tmdb/', views.tmdb_movies),
]