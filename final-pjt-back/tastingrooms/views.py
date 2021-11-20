from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# model
from .models import TastingTag, Tastingroom
from movies.models import Movie
from django.contrib.auth import get_user_model

# serializer
from .serializers import TastingroomSerializer, TastingroomListSerializer

# orm
from django.db.models import Q, Count

# login user
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# logic
import random
from datetime import timedelta


# 추천기준 정해야함 (화면 표시 데이터만 넘기기)
# basket을 작성해보고 복붙


@api_view(['POST'])
def tastingroom_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    author = get_object_or_404(get_user_model(), pk=request.user.pk)

    # author = get_object_or_404(get_user_model(), pk=2)
    serializer = TastingroomSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            movie=movie,
            author=author,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# tastingroom detail, update, delete
@api_view(['GET', 'PUT', 'DELETE'])
def tastingroom_detail_update_delete(request, tastingroom_pk, movie_pk):
    tastingroom = get_object_or_404(Tastingroom, pk=tastingroom_pk)

    if request.method == 'GET':
        serializer = TastingroomSerializer(tastingroom)
        return Response(serializer.data)

    elif request.method == 'PUT':
        movie = get_object_or_404(Movie, pk=movie_pk)
        author = get_object_or_404(get_user_model(), pk=request.user.pk)
        serializer = TastingroomSerializer(instance=tastingroom, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                movie=movie,
                author=author,
            )
            return Response(serializer.data)

    elif request.method == 'DELETE':
        tastingroom.delete()
        data = {
            'delete': '테이스팅룸이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    

# tastingroom search (index, 영화섹션용) (검색어 필터링해서 다 보여주는거) 참여자명, 채팅방명, 채팅태그명, (참여자수 정렬)
@api_view(['GET'])
def tastingroom_search(request, query):
    q = Q()
    q.add(
        Q(participants__nickname__icontains=query)|
        Q(title__icontains=query)|
        Q(tags__name__icontains=query),
        q.OR
    )
    q.add(
        Q(public=True)|
        Q(participants__nickname__icontains=request.user.nickname),
        q.AND
    )
    tastingrooms = Tastingroom.objects.filter(q).distinct().annotate(participants_count=Count('participants')).order_by('-participants_count')
    serializer = TastingroomListSerializer(tastingrooms, many=True)
    return Response(serializer.data)


def tastingroom_recommend_myinfo(request):
    start_date = request.user.birthdate - timedelta(years=5)
    end_date = request.user.birthdate + timedelta(years=5)

    filtered_tastingroom_ids = list(Tastingroom.objects.all().filter(
        participants__birthdate__range=(start_date, end_date),
        participants__gender=request.user.gender,
        public=True
        ).distinct().values('id'))

    if len(filtered_tastingroom_ids) >= 6:
        picked_tastingroom_ids = random.sample(filtered_tastingroom_ids, 6)
    else: # 6개 미만일때는 그냥 전체 랜덤으로
        picked_tastingroom_ids = random.sample(list(Tastingroom.objects.all(), 6))
    picked_tastingrooms = Tastingroom.objects.filter(pk__in=picked_tastingroom_ids)    

    serializer = TastingroomListSerializer(picked_tastingrooms, many=True)
    return Response(serializer.data)


def tastingroom_recommend_movies(request):
    random_movie = random(request.user.like_movies)

    filtered_tastingroom_ids = list(Tastingroom.objects.all().filter(
        movie__id=random_movie
    ).distinct().values('id'))

    if len(filtered_tastingroom_ids) >= 6:
        picked_tastingroom_ids = random.sample(filtered_tastingroom_ids, 6)
    else: # 6개 이하일때는 그냥 전체 랜덤으로
        picked_tastingroom_ids = random.sample(list(Tastingroom.objects.all(), 6))
    picked_tastingroom = Tastingroom.objects.filter(pk__in=picked_tastingroom_ids)    

    serializer = TastingroomListSerializer(picked_tastingroom, many=True)
    return Response(serializer.data)


def tastingroom_recommend_tags(request):
    random_tag = random(request.user.users_basket_tags)

    filtered_tastingroom_ids = list(Tastingroom.objects.all().filter(
        tags__icontains=random_tag
    ).distinct().values('id'))

    if len(filtered_tastingroom_ids) >= 6:
        picked_tastingroom_ids = random.sample(filtered_tastingroom_ids, 6)
    else: # 6개 이하일때는 그냥 전체 랜덤으로
        picked_tastingroom_ids = random.sample(list(Tastingroom.objects.all(), 6))
    picked_tastingroom = Tastingroom.objects.filter(pk__in=picked_tastingroom_ids)    

    serializer = TastingroomListSerializer(picked_tastingroom, many=True)
    return Response(serializer.data)


def tastingroom_recommend_friends(request):
    friends = list(request.user.stars.values('id')) # 랜덤으로 1명 뽑는 거 말고 전체 친구로 해도 괜찮을듯

    filtered_tastingroom_ids = list(Tastingroom.objects.all().filter(
        participants__id__in=[friend for friend in friends],
        public=True 
    ).distinct().values('id'))

    if len(filtered_tastingroom_ids) >= 6:
        picked_tastingroom_ids = random.sample(filtered_tastingroom_ids, 6)
    else: # 6개 이하일때는 그냥 전체 랜덤으로
        picked_tastingroom_ids = random.sample(list(Tastingroom.objects.all(), 6))
    picked_tastingroom = Tastingroom.objects.filter(pk__in=picked_tastingroom_ids)    

    serializer = TastingroomListSerializer(picked_tastingroom, many=True)
    return Response(serializer.data)


