from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.basket_create),
    path('<int:basket_pk>/', views.basket_detail),
    path('<int:basket_pk>/comment/create', views.comment_create),
    path('<int:basket_pk>/comment/<int:comment_pk>', views.comment_detail),

    # 추천로직: 연령성별, 선호영화, 태그, 팔로한사람이좋아한
    path('recommend/myself', views.basket_recommend_myself),
    path('recommend/movies', views.basket_recommend_movies),
    path('recommend/tags', views.basket_recommend_tags),
    path('recommend/friend', views.basket_recommend_friends),
]
