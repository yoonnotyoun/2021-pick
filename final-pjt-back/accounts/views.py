from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# model
from django.contrib.auth import get_user_model
from accounts.models import Group, Relationship

# serializer
from .serializers import GroupListSerialzier, GroupSerialzier, RelationshipListSerializer, RelationshipSerializer, UserSerializer

# login user
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication




# 회원가입 가져오기 (기본그룹 생성)
@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        # Group.objects.get(pk=1).user.add(user) # 기본 그룹생성
        Group.objects.create(user=user) # 기본 그룹생성

    return Response(serializer.data, status=status.HTTP_201_CREATED)


# profile에서 유저와 관련된 데이터 다 가져와야됨
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        image = request.data.get('image') # 필수인지 확인
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(image=image)
            return Response(serializer.data)
    elif request.method == 'DELETE':
        user_pk = request.user.pk
        request.user.delete()
        return Response({ 'delete': f'{user_pk} 회원이 탈퇴했습니다.' }, status=status.HTTP_204_NO_CONTENT)


# Group (CRD)
# RC
@api_view(['GET', 'POST'])
def group_list_create(request):
    if request.method == 'GET':
        groups = Group.objects.filter(user=1)
        # groups = Group.objects.filter(user=request.user.pk)
        serializer = GroupListSerialzier(groups, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        user = get_object_or_404(get_user_model(), pk=1)
        # user = get_object_or_404(get_user_model(), pk=request.user.pk)
        serializer = GroupSerialzier(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                user = user,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# D
@api_view(['DELETE'])
def group_delete(request, group_pk):
    group = Group.objects.filter(pk=group_pk)
    group.delete()
    data = {
        'delete': '그룹이 삭제되었습니다.'
    }
    return Response(data, status=status.HTTP_204_NO_CONTENT)


# Relationship (RU)# 새 그룹 생성 없이 팔로잉 그룹 관리 (해당 유저의 relationship)
# Relationship R
@api_view(['GET'])
def relationship_list(request):
    relationships = Relationship.objects.filter(fan=1)
    # relationships = Relationship.objects.filter(fan=request.user.pk)
    serializer = RelationshipListSerializer(relationships, many=True)
    return Response(serializer.data)


# Follow
# '기본' 그룹으로 들어가게
@api_view(['POST'])
def relationship_create(request, star_pk):
    fan = get_object_or_404(get_user_model(), pk=1)
    # fan = request.user
    star = get_object_or_404(get_user_model(), pk=star_pk)
    group = get_object_or_404(Group, user=fan, name='기본') # 기본 그룹

    if fan != star:
        # POST (팔로우)
        serializer = RelationshipSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                fan=fan,
                star=star,
                group=group,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Relationship UD (그룹 이동, 팔로우 취소)
@api_view(['PUT', 'DELETE'])
def relationship_update_delete(request, relationship_pk, star_pk, group_pk):
    relationship = get_object_or_404(Relationship, pk=relationship_pk)
    fan = get_object_or_404(get_user_model(), pk=1)
    # fan = get_object_or_404(get_user_model(), pk=request.user.pk)
    star = get_object_or_404(get_user_model(), pk=star_pk)

    if request.method == 'PUT':
        group = get_object_or_404(Group, pk=group_pk)
        serializer = RelationshipSerializer(instance=relationship, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                fan=fan,
                star=star,
                group=group,
            )
            return Response(serializer.data)

    elif request.method == 'DELETE':
        if star.fans.filter(pk=fan.pk).exists():
            relationship.delete()
            data = {
                'delete': '언팔로우 처리되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
