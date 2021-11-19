from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Basket, Comment, BasketTag
from .serializers import BasketListSerializer, BasketSerializer, CommentSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import random


@api_view(['POST'])
def basket_create(request):
    serializer = BasketSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        basket = serializer.save(
            author=request.user,
            # movies=
            )
        for word in basket.content.split():
            if word.startswith('#'):
                tag, created = BasketTag.objects.get_or_create(content=word)
                basket.basket_tags.add(tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def basket_detail(request, basket_pk):
    basket = get_object_or_404(Basket, pk=basket_pk)
    if request.method == 'GET':
        serializer = BasketSerializer(basket)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BasketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            basket.basket_tags.clear()
            for word in basket.content.split():
                if word.startswith('#'):
                    tag, created = BasketTag.objects.get_or_create(content=word)
                    basket.basket_tags.add(tag)
    else:
        basket.delete()
        data = {
            'delete': '바스켓이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


def comment_create(request, basket_pk):
    basket = get_object_or_404(Basket, pk=basket_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(author=request.user, basket=basket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def comment_detail(request, basket_pk, comment_pk):
    basket = get_object_or_404(Basket, pk=basket_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.author:
        if request.method == 'DELETE':
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
