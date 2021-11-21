from rest_framework import serializers
from django.contrib.auth import get_user, get_user_model

from .models import Group, Relationship
from movies.models import Movie
from baskets.models import Basket, BasketTag, Comment
from tastingrooms.models import Tastingroom


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'poster_path', 'title', 'release_date', 'vote_average',)

    class BasketListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Basket
            fields = ('id', 'image', 'title', 'author', 'basket_tags',)

    class CommentListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'

    class BasketTagListSerializer(serializers.ModelSerializer):
        class Meta:
            model = BasketTag
            fields = '__all__'

    class TastingroomListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tastingroom
            fields = ('id', 'name',)

    like_movies = MovieListSerializer(many=True, required=False, read_only=True)
    author_baskets = BasketListSerializer(many=True, required=False, read_only=True)
    like_baskets = BasketListSerializer(many=True, required=False, read_only=True)
    participating_baskets = BasketListSerializer(many=True, required=False, read_only=True)
    author_comments = CommentListSerializer(many=True, required=False, read_only=True)
    users_basket_tags = BasketTagListSerializer(many=True, required=False, read_only=True)
    author_tastingrooms = TastingroomListSerializer(many=True, required=False, read_only=True)
    participating_tastingrooms = TastingroomListSerializer(many=True, required=False, read_only=True)
    
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
        fields = ('id', 'name',)


class GroupSerialzier(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ('user',)


class RelationshipListSerializer(serializers.ModelSerializer):
    
    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = get_user_model()
    #         fields = '__all__'

    # class GroupSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Group
    #         fields = '__all__'

    # star = UserSerializer()
    # fan = UserSerializer()
    # group = GroupSerializer()
    
    class Meta:
        model = Relationship
        fields = '__all__'
        read_only_fields = '__all__'


class RelationshipSerializer(serializers.ModelSerializer):
    
    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = get_user_model()
    #         fields = '__all__'

    # class GroupSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Group
    #         fields = '__all__'

    # star = UserSerializer()
    # fan = UserSerializer()
    # group = GroupSerializer()
    
    class Meta:
        model = Relationship
        fields = '__all__'
        read_only_fields = '__all__'