from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from movies.models import Movie

from .models import Basket, Comment, BasketTag
from .serializers import BasketListSerializer, BasketSerializer, CommentSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import random


@api_view(['POST'])
def basket_create(request):
    movies = get_list_or_404(Movie)
    author = get_object_or_404(get_user_model(), pk=request.user.pk)

    serializer = BasketSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            author = author,
            movies = movies,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def basket_detail_update_delete(request, basket_pk):
    basket = get_object_or_404(Basket, pk=basket_pk)

    if request.method == 'GET':
        serializer = BasketSerializer(basket)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        movies = get_list_or_404(Movie)
        author = get_object_or_404(get_user_model(), pk=request.user.pk)
        serializer = BasketSerializer(instance=basket, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                movies=movies,
                author=author,
            )
            return Response(serializer.data)

    elif request.method == 'DELETE':
        basket.delete()
        data = {
            'delete': '바스켓이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def comment_list_create(request, basket_pk):

    if request.method == 'GET':
        comments = get_list_or_404(Comment, basket=basket_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        basket = get_object_or_404(Basket, pk=basket_pk)
        author = get_object_or_404(get_user_model(), pk=request.user.pk)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                author=author,
                basket=basket,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user == comment.author:
        comment.delete()
        data = {
            'delete' : f'{comment_pk}번 댓글이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


def basket_recommend_myself(request):
    pass


def basket_recommend_movies(request):
    pass


def basket_recommend_tags(request):
    random_tags = random(request.user.users_basket_tags)



def basket_recommend_friends(request):
    random_stars = random.sample(list(request.user.stars.values('id')))
    baskets = Basket.objects.filter() #random_star가 좋아요를 누른 거
    serializers = BasketListSerializer(baskets, many=True)





# 추천기준 6가지 반영해서 데이터 넘기기 (함수각각) (index, basket섹션용)

# 연령성별
# 선호영화(가 들어있는 다른 바스켓)
# 좋아요한 태그 기반
# 팔로한 사람이 좋아한 바스켓

# search

# detail
