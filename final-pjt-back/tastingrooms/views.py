from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# model
from .models import TastingTag, Tastingroom
from movies.models import Movie
from django.contrib.auth import get_user_model

# serializer
from .serializers import TastingTagSerializer, TastingroomSerializer, TastingroomListSerializer

# orm
from django.db.models import Q, Count

# login user
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# 추천기준 정해야함 (화면 표시 데이터만 넘기기)
# basket을 작성해보고 복붙

@api_view(['POST'])
def create_track(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    serializer = TrackSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(album=album)
        return Response(serializer.data)
# tastingroom create
@api_view(['POST'])
def tastingroom_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    author = get_object_or_404(get_user_model(), pk=request.user.pk)
    serializer = TastingroomSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            movie=movie,
            author=author,
        )
        # for word in serializer.cont.split():
        #     if word.startswith('#'):
        #         tag, created = BasketTag.objects.get_or_create(content=word)
        #         basket.basket_tags.add(tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# tastingroom search (index, 영화섹션용) (검색어 필터링해서 다 보여주는거) 참여자명, 채팅방명, 채팅태그명, (참여자수 정렬)
@api_view(['GET'])
def tastingrooms_search(request, query):
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


# tastingroom detail
@api_view(['GET'])
def tastingroom_detail(request, tastingroom_pk):
    tastingroom = Tastingroom.objects.get(pk=tastingroom_pk)
    serializer = TastingroomSerializer(tastingroom)
    return Response(serializer.data)
    