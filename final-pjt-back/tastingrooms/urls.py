from django.urls import path
from . import views

urlpatterns = [
    # 테이스팅룸 기본 기능
    path('<int:movie_pk>/', views.tastingroom_create),
    path('movies/<int:movie_pk>/tastingrooms/<int:tastingroom_pk>/', views.tastingroom_detail_update_delete),
    
    # 추천로직: 연령성별, 선호영화, 바스켓태그, 팔로한사람(들)이참여중인
    path('recommend/myinfo', views.tastingroom_recommend_myinfo),
    path('recommend/movies', views.tastingroom_recommend_movies),
    path('recommend/tags', views.tastingroom_recommend_tags),
    path('recommend/friends', views.tastingroom_recommend_friends),

    # 검색
    path('search/<query>/', views.tastingroom_search),
]
