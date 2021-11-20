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


