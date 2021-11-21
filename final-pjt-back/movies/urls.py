from django.urls import path
from . import views

urlpatterns = [
    # 영화 기본 기능
    path('search/<query>/', views.movies_search),
    path('<int:movie_pk>/', views.movie_detail),

    # 추천로직
    # 연령성별, 좋아한 바스켓, 친구가 좋아한 영화
    path('recommend/myinfo', views.movie_recommend_myinfo),
    path('recommend/baskets', views.movie_recommend_baskets),
    path('recommend/friends', views.movie_recommend_friends),

    # tmdb api
    path('tmdb/', views.tmdb_movies),
]