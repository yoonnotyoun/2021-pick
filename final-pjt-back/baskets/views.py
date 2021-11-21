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


# 성별, 연령
@api_view(['GET'])
def basket_recommend_myinfo(request):
    start_date = request.user.birthdate - timedelta(years=5)
    end_date = request.user.birthdate + timedelta(years=5)

    filtered_basket_ids = list(Basket.objects.all().filter(
        like_users__birthdate__range=(start_date, end_date),
        like_users__gender=request.user.gender
        ).distinct().order_by('-vote_average').values('id')) # 생각해보니까 어차피 랜덤 할 건데 orderby 필요한가? => 안필요한데 어제 까먹은듯!

    if len(filtered_basket_ids) >= 3:
        picked_basket_ids = random.sample(filtered_basket_ids, 3)
    else: # 3개 이하일때는 그냥 전체 랜덤으로 => 굳굳
        picked_basket_ids = random.sample(list(Basket.objects.all(), 3)) # 이거 values('id') 추가!
    picked_baskets = Basket.objects.filter(pk__in=picked_basket_ids)    

    serializer = BasketSerializer(picked_baskets, many=True) # 여기 BasketListSerializer 아닌가 싶음! => 맞아!!
    return Response(serializer.data)


# 선호 영화가 들어있는
def basket_recommend_movies(request):
    # random_movie_id = random.choice(request.user.like_movies) # 이거랑 아래 중에 뭔지 잘 모르겠음
    random_movie_id = random.choice(list(request.user.like_movies.values('id'))) # => 이게 맞는듯!

    # filtered_basket_ids = list(Basket.objects.all().filter(
    #     movies__id=random_movie_id
    # ).distinct().order_by('-vote_average').values('id')) # => .all()없어도 될듯?? 그리고 지금 알아낸 건데 vote_average는 movie용이고 우리는 like_users Count 순으로 하거나 order_by는 안하거나 하면될거같다. 우선 이거 하나만 내가 바꿔봄.
    filtered_basket_ids = list(Basket.objects.all().filter(
        movies__id=random_movie_id
        ).distinct().order_by('-vote_average').values('id')).annotate(like_users_count=Count('like_users')).order_by('-like_users_count')
    
    if len(filtered_basket_ids) >= 3:
        picked_basket_ids = random.sample(filtered_basket_ids, 3)
    else: # 3개 이하일때는 그냥 전체 랜덤으로
        picked_basket_ids = random.sample(list(Basket.objects.all(), 3)) # 이거 values('id') 추가!
    picked_baskets = Basket.objects.filter(pk__in=picked_basket_ids)    

    serializer = BasketSerializer(picked_baskets, many=True)
    return Response(serializer.data)


# 좋아하는 태그가 들어있는 -> 좋아하는 태그 로직부터 구현해야할 것 같지만
def basket_recommend_tags(request):
    random_tag = random(request.user.users_basket_tags) # 리스트로 랜덤처리로 id 뽑아낸 후 아래에서는 icontains가 아니라 basket_tags__pk=random_tag_id로 가면 되지 않을까 하는 생각

    filtered_basket_ids = list(Basket.objects.all().filter(
        basket_tags__icontains=random_tag
    ).distinct().order_by('-vote_average').values('id')) # 여기도 위와 같은 피드백(all(), order_by, tag_id)

    if len(filtered_basket_ids) >= 3:
        picked_basket_ids = random.sample(filtered_basket_ids, 3)
    else: # 3개 이하일때는 그냥 전체 랜덤으로
        picked_basket_ids = random.sample(list(Basket.objects.all(), 3))
    picked_baskets = Basket.objects.filter(pk__in=picked_basket_ids)    

    serializer = BasketSerializer(picked_baskets, many=True)
    return Response(serializer.data)


def basket_recommend_friends(request):
    random_star = random.sample(list(request.user.stars.values('id')))

    filtered_basket_ids = list(Basket.objects.all().filter(
        like_users__id=random_star
    ).distinct().order_by('-vote_average').values('id'))

    if len(filtered_basket_ids) >= 3:
        picked_basket_ids = random.sample(filtered_basket_ids, 3)
    else: # 3개 이하일때는 그냥 전체 랜덤으로
        picked_basket_ids = random.sample(list(Basket.objects.all(), 3))
    picked_baskets = Basket.objects.filter(pk__in=picked_basket_ids)    

    serializer = BasketSerializer(picked_baskets, many=True)
    return Response(serializer.data)


# basket search (index, 바스켓섹션용)
def basket_search(request, query):
    q = Q()
    q.add(
        Q(title__icontains=query)|
        Q(basket_tags__name__icontains=query)|
        Q(participants__nickname__icontains=query),
        q.OR
    )
    q.add(
        Q(public=True)|
        Q(participants__nickname__icontains=request.user.nickname),
        q.AND
    )
    tastingrooms = Basket.objects.filter(q).distinct().annotate(participants_count=Count('participants')).order_by('-participants_count')
    serializer = BasketListSerializer(tastingrooms, many=True)
    return Response(serializer.data)