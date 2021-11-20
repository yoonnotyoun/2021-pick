from django.urls import path
from . import views

urlpatterns = [
    # 테이스팅룸 기본 기능
    path('create/<int:movie_pk>/', views.tastingroom_create),
    path('search/<query>/', views.tastingrooms_search),
    path('<int:tastingroom_pk>/', views.tastingroom_detail),
]
