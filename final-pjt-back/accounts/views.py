from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


# profile에서 유저와 관련된 데이터 다 가져와야됨

# 회원가입 가져오기
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
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# Follow
# '기본' 그룹으로 들어가게 relationship serializer??? 모르겠솨


# Group (CRD)
# RC
# D


# Relationship (RU)# 새 그룹 생성 없이 팔로잉 그룹 관리 (해당 유저의 relationship)
# 추가
# 그룹 이동