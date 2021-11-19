from rest_framework import serializers
from django.contrib.auth import get_user, get_user_model
from baskets.serializers import BasketListSerializer, BasketTagListSerializer, CommentListSerializer

from movies.serializers import MovieListSerializer
from tastingrooms.serializers import TastingroomListSerializer
from .models import Group, Relationship


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # stars = 
    # fans = 
    like_movies = MovieListSerializer(many=True)
    author_baskets = BasketListSerializer(many=True)
    like_baskets = BasketListSerializer(many=True)
    participating_baskets = BasketListSerializer(many=True)
    author_comments = CommentListSerializer(many=True)
    users_basket_tags = BasketTagListSerializer(many=True)
    author_tastingrooms = TastingroomListSerializer(many=True)
    participating_tastingrooms = TastingroomListSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'password', 'stars', 'fans', 'nickname', 'birthdate', 'gender', 'image',
            'like_movies', 'author_baskets', 'like_baskets', 'participating_baskets',
            'author_comments', 'users_basket_tags', 'author_tastingrooms', 'participating_tastingrooms',
            )
        read_only_fields = (
            'stars', 'fans', 'like_movies', 'author_baskets', 'like_baskets', 'participating_baskets',
            'author_comments', 'users_basket_tags', 'author_tastingrooms', 'participating_tastingrooms',
            )


class GroupListSerialzier(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('name',)


class GroupSerialzier(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ('user',)


class RelationshipSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'

    class GroupSerializer(serializers.ModelSerializer):
        class Meta:
            model = Group
            fields = '__all__'

    star = UserSerializer()
    fan = UserSerializer()
    group = GroupSerializer()
    
    class Meta:
        model = Relationship
        fields = '__all__'
        read_only_fields = '__all__'