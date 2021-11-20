from django.urls import path
from . import views

urlpatterns = [
    # 테이스팅룸 기본 기능
    path('<int:movie_pk>/', views.tastingroom_create),
    path('movies/<int:movie_pk>/tastingrooms/<int:tastingroom_pk>/', views.tastingroom_detail_update_delete),
    path('search/<query>/', views.tastingroom_search),
]
