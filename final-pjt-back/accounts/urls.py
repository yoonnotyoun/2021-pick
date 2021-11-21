from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # 로그인/회원가입
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('profile/', views.profile),

    # 그룹 관리
    # path('group/', views.group_list_create),
    # path('group/<int:group_pk>/', views.group_delete),
    # path('relationship/', views.relationship_list),
    # path('relationship/<int:relationship_pk>/<int:group_pk>/', views.relationship_update),

    # # 팔로우
    # path('<int:star_pk>/follow/', views.follow),
]