from django.urls import path
from . import views

urlpatterns = [
    # path('db/genres/', views.db_genres),
    # path('db/actors/', views.db_actors),
    path('db/movies/', views.db_movies),
]
