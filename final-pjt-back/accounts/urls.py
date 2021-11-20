from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),

    # path('<int:user_pk>/group', views.group),
    # path('<int:user_pk>/follow/', views.follow),
    path('profile/', views.profile),
    # path('<int:user_pk>/relationship/', views.relationship),
]
