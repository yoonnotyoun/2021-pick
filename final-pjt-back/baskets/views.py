from datetime import timedelta
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from movies.models import Movie

# REST framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# orm
from django.db.models import Q, Count

from .models import Basket, Comment, BasketTag
from .serializers import BasketListSerializer, BasketSerializer, CommentSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# 추천 로직
import random


@api_view(['POST'])
def basket_create(request):
    # movies = get_list_or_404(Movie) 첫번째 에러 이거 외래키라 여기서 처리하는 거 아님...
    # author = get_object_or_404(get_user_model(), pk=request.user.pk)
    author = get_object_or_404(get_user_model(), pk=1)

    serializer = BasketSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            author = author,
            # movies = movies,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def basket_detail_update_delete(request, basket_pk):
    basket = get_object_or_404(Basket, pk=basket_pk)

    if request.method == 'GET':
        serializer = BasketSerializer(basket)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        # movies = get_list_or_404(Movie)
        # author = get_object_or_404(get_user_model(), pk=request.user.pk)
        author = get_object_or_404(get_user_model(), pk=1)
        
        serializer = BasketSerializer(instance=basket, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                # movies=movies,
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


# 성별, 연령 기준 추천
@api_view(['GET'])
def basket_recommend_myinfo(request):
    start_date = request.user.birthdate - timedelta(years=5)
    end_date = request.user.birthdate + timedelta(years=5)
    # public이거나 participants에 user가 포함된 경우만
    q = Q()
    q.add(
        Q(like_users__birthdate__range=(start_date, end_date)),
        q.AND
    )
    q.add(
        Q(like_users__gender=request.user.gender),
        q.AND
    )
    q.add(
        Q(public=True)|
        Q(participants__pk=request.user.pk),
        q.AND
    )
    filtered_basket_ids = Basket.objects.filter(q).distinct().values('id')

    if len(filtered_basket_ids) >= 3:
        picked_basket_ids = random.sample(filtered_basket_ids, 3)
    else: # 3개 이하일때는 그냥 전체 랜덤으로
        picked_basket_ids = random.sample(list(Basket.objects.all().values('id'), 3))
    picked_baskets = Basket.objects.filter(pk__in=picked_basket_ids).annotate(like_users_count=Count('like_users')).order_by('-like_users_count')

    serializer = BasketListSerializer(picked_baskets, many=True)

    return Response(serializer.data)


# 선호 영화가 들어있는 기준 추천
@api_view(['GET'])
def basket_recommend_movies(request):
    random_movie_id = random.sample(list(request.user.like_movies.values('id')))
    # public이거나 participants에 user가 포함된 경우만
    q = Q()
    q.add(
        Q(movies__id=random_movie_id),
        q.OR
    )
    q.add(
        Q(public=True)|
        Q(participants__pk=request.user.pk),
        q.AND
    )
    filtered_basket_ids = Basket.objects.filter(q).distinct().values('id')
    
    if len(filtered_basket_ids) >= 3:
        picked_basket_ids = random.sample(filtered_basket_ids, 3)
    else: # 3개 이하일때는 그냥 전체 랜덤으로
        picked_basket_ids = random.sample(list(Basket.objects.all().values('id'), 3)) # 이거 values('id') 추가!
    picked_baskets = Basket.objects.filter(pk__in=picked_basket_ids).annotate(like_users_count=Count('like_users')).order_by('-like_users_count')

    serializer = BasketListSerializer(picked_baskets, many=True)

    return Response(serializer.data)


# 좋아하는 태그가 들어있는 기준 추천 -> 좋아하는 태그 로직부터 구현해야할 것 같지만
@api_view(['GET'])
def basket_recommend_tags(request):
    random_tag_id = random.sample(list(request.user.users_basket_tags.values('id')))
    # public이거나 participants에 user가 포함된 경우만
    q = Q()
    q.add(
        Q(basket_tags__pk=random_tag_id),
        q.OR
    )
    q.add(
        Q(public=True)|
        Q(participants__pk=request.user.pk),
        q.AND
    )
    filtered_basket_ids = Basket.objects.filter(q).distinct().values('id')

    if len(filtered_basket_ids) >= 3:
        picked_basket_ids = random.sample(filtered_basket_ids, 3)
    else: # 3개 이하일때는 그냥 전체 랜덤으로
        picked_basket_ids = random.sample(list(Basket.objects.all().values('id'), 3))
    picked_baskets = Basket.objects.filter(pk__in=picked_basket_ids).annotate(like_users_count=Count('like_users')).order_by('-like_users_count')

    serializer = BasketListSerializer(picked_baskets, many=True)

    return Response(serializer.data)


# 팔로우하는 유저가 좋아한 기준 추천
@api_view(['GET'])
def basket_recommend_friends(request):
    random_star_id = random.sample(list(request.user.stars.values('id')))
    # public이거나 participants에 user가 포함된 경우만
    q = Q()
    q.add(
        Q(like_users__id=random_star_id),
        q.OR
    )
    q.add(
        Q(public=True)|
        Q(participants__pk=request.user.pk),
        q.AND
    )
    filtered_basket_ids = Basket.objects.filter(q).distinct().values('id')

    if len(filtered_basket_ids) >= 3:
        picked_basket_ids = random.sample(filtered_basket_ids, 3)
    else: # 3개 이하일때는 그냥 전체 랜덤으로
        picked_basket_ids = random.sample(list(Basket.objects.all().values('id'), 3))
    picked_baskets = Basket.objects.filter(pk__in=picked_basket_ids).annotate(like_users_count=Count('like_users')).order_by('-like_users_count')  

    serializer = BasketListSerializer(picked_baskets, many=True)

    return Response(serializer.data)


# basket search (index, 바스켓섹션용) 바스켓 제목, 바스켓 태그, 작성자, 영화명, 배우 (추천순)
@api_view(['GET'])
def basket_search(request, query):
    q = Q()
    q.add(
        Q(title__icontains=query)|
        Q(baskets_tags__name__icontains=query)|
        Q(author__nickname__icontains=query)|
        Q(movies__title__icontains=query)|
        Q(movies__actors__name__icontains=query)|
        Q(movies__genres__name__icontains=query),
        q.OR
    )
    q.add(
        # Q(public=True),
        Q(public=True)|
        Q(participants__nickname__icontains=request.user.nickname),
        q.AND
    )

    baskets = Basket.objects.filter(q).distinct().annotate(like_users_count=Count('like_users')).order_by('-like_users_count')
    serializer = BasketListSerializer(baskets, many=True)

    return Response(serializer.data)


# 좋아요 기능
@api_view(['POST'])
def basket_like(request, basket_pk):
    basket = get_object_or_404(Basket, pk=basket_pk)

    # user = get_object_or_404(get_user_model(), pk=1)
    # if basket.like_users.filter(pk=user.pk).exists():
    #     basket.like_users.remove(user)
    #     liked = False
    # else:
    #     basket.like_users.add(user)
    #     liked = True

    if basket.like_users.filter(pk=request.user.pk).exists():
        basket.like_users.remove(request.user)
        liked = False
    else:
        basket.like_users.add(request.user)
        liked = True
    data = {
        'basket': basket_pk,
        'liked': liked,
        'cnt_likes': basket.like_users.count(),
    }
    return Response(data, status=status.HTTP_204_NO_CONTENT)