from rest_framework import serializers

from .models import Basket, Comment, BasketTag
from movies.models import Movie
from django.contrib.auth import get_user_model

# accounts: author_nickname, author_img
# content, spoiler, created_at
class CommentListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            models = get_user_model()
            fields = ('nickname', 'image',)

    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'basket', 'content', 'spoiler',)
        read_only_fields = ('author', 'basket',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('basket', 'author',)


class BasketTagListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketTag
        fields = ('id', 'name', 'baskets',)


class BasketTagSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'nickname',)

    class BasketSerializer(serializers.ModelSerializer):
        class Meta:
            model = Basket
            fields = ('id', 'title',)

    users = UserSerializer(many=True)
    baskets = BasketSerializer(many=True)

    class Meta:
        model = BasketTag
        fields = '__all__'
        read_only_fields = ('users', 'baskets',)


#(title, author, tags, like_users개수, img)
class BasketListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            models = get_user_model()
            fields = ('id', 'nickname', 'image',)

    like_users = UserSerializer(many=True, required=False)
    basket_tags = BasketTagListSerializer(many=True, required=False)

    class Meta:
        model = Basket
        fields = ('id', 'title', 'author', 'image', 'like_users', 'basket_tags',)
        read_only_fields = ('author', 'like_users', 'basket_tags',)


# accounts에서 가져올 author 정보 (author_nickname, author_img, author_fans)
# 그 외 직접 가져올 정보 (img, public, title, basket_tags, explanation, like_users프로필 이미지, movies, basket_comments)
class BasketSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'nickname', 'image', 'fans',) # fans 받아올 수 있는가?

    class BasketTagListSerializer(serializers.ModelSerializer):
        class Meta:
            model = BasketTag
            fields = ('id', 'name',)

    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            models = Movie
            fields = ('id', 'title',)

    author = UserSerializer(required=False)
    basket_tags = BasketTagListSerializer(many=True, required=False)
    movies = MovieListSerializer(many=True, required=False)
    like_users = UserSerializer(many=True, required=False)
    participants = UserSerializer(many=True, required=False)

    class Meta:
        model = Basket
        fields = (
            'id', 'image', 'public', 'title', 'explanation', 'movies', 'created_at', 'updated_at',
            'author', 'like_users', 'participants', 'basket_tags',
        )
        read_only_fields = ('author', 'movies', 'like_users', 'participants', 'basket_tags',)