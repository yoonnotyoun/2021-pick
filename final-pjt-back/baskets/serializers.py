from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Basket, Comment, BasketTag
from movies.models import Movie
from django.contrib.auth import get_user_model


# # 바스켓태그 여러개 R
# class BasketTagListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = BasketTag
#         fields = ('id', 'name', 'baskets',)


# # 바스켓 태그 CUD
# class BasketTagSerializer(serializers.ModelSerializer):

#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = get_user_model()
#             fields = ('id', 'nickname',)

#     class BasketSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Basket
#             fields = ('id', 'title',)

#     users = UserSerializer(many=True, read_only=True)
#     baskets = BasketSerializer(many=True, read_only=True)

#     class Meta:
#         model = BasketTag
#         fields = '__all__'
#         read_only_fields = ('users', 'baskets',)


#(title, author, tags, like_users개수, img)
# 바스켓 여러개 R
class BasketListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            models = get_user_model()
            fields = ('id', 'nickname', 'image',)

    class BasketTagListSerializer(serializers.ModelSerializer):

        class Meta:
            model = BasketTag
            fields = ('id', 'name', 'baskets',)

    like_users = UserSerializer(many=True, required=False, read_only=True)
    basket_tags = BasketTagListSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Basket
        fields = ('id', 'title', 'author', 'image', 'like_users', 'basket_tags',)
        read_only_fields = ('author', 'like_users', 'basket_tags',)


# accounts에서 가져올 author 정보 (author_nickname, author_img, author_fans)
# 그 외 직접 가져올 정보 (img, public, title, basket_tags, explanation, like_users프로필 이미지, movies, basket_comments)
# 바스켓 CUD
class BasketSerializer(serializers.ModelSerializer):

    class BasketTagListSerializer(serializers.ModelSerializer):
        class Meta:
            model = BasketTag
            fields = ('id', 'name',)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'nickname', 'image', 'fans',)

    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            models = Movie
            fields = ('id', 'title',)

    basket_tags = BasketTagListSerializer(many=True, required=False, read_only=True) # 역참조
    like_users = UserSerializer(many=True, required=False, read_only=True)
    participants = UserSerializer(many=True, required=False, read_only=True)
    movies = MovieListSerializer(many=True, required=False, read_only=True)

    # Vue에서 보내줄 추가 데이터
    basket_tags_names = serializers.ListField(write_only=True)
    participants_ids = serializers.ListField(write_only=True)
    movies_ids = serializers.ListField(write_only=True)

    class Meta:
        model = Basket
        fields = (
            'id', 'image', 'public', 'title', 'explanation', 'movies', 'created_at', 'updated_at',
            'author', 'like_users', 'participants', 'baskets_tags',
        )
        read_only_fields = ('author', 'like_users',)

    def create(self, validated_data):
        basket_tags_names = validated_data.pop('basket_tags_names')
        participants_ids = validated_data.pop('participants_ids')
        movies_ids = validated_data.pop('movies_ids')
        basket = Basket.objects.create(**validated_data)
        
        for basket_tags_name in basket_tags_names:
            if BasketTag.objects.filter(name=basket_tags_name).exists():
                basket_tag = get_object_or_404(BasketTag, name=basket_tags_name)
            else:
                basket_tag = BasketTag.objects.create(name=basket_tags_name)
            basket.baskets_tags.add(basket_tag)
        for participants_id in participants_ids:
            participant = get_user_model().objects.get(pk=participants_id)
            basket.participants.add(participant)
        for movies_id in movies_ids:
            movie = Movie.objects.get(pk=movies_id)
            basket.movies.add(movie)

        return basket

    def update(self, basket, validated_data):
        basket_tags_names = validated_data.pop('basket_tags_names')
        participants_ids = validated_data.pop('participants_ids')
        movies_ids = validated_data.pop('movies_ids')
        basket = Basket.objects.create(**validated_data)

        for attr, value in validated_data.items():
            setattr(basket, attr, value)
        basket.save()

        basket.baskets_tags.clear()
        basket.participants.clear()
        basket.movies.clear()

        for basket_tags_name in basket_tags_names:
            if BasketTag.objects.filter(name=basket_tags_name).exists():
                basket_tag = get_object_or_404(BasketTag, name=basket_tags_name)
            else:
                basket_tag = BasketTag.objects.create(name=basket_tags_name)
            basket.baskets_tags.add(basket_tag)
        for participants_id in participants_ids:
            participant = get_user_model().objects.get(pk=participants_id)
            basket.participants.add(participant)
        for movies_id in movies_ids:
            movie = Movie.objects.get(pk=movies_id)
            basket.movies.add(movie)

        return basket


# accounts: author_nickname, author_img
# content, spoiler, created_at
# 댓글 여러개
class CommentListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            models = get_user_model()
            fields = ('nickname', 'image',)

    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'basket', 'content', 'spoiler',)
        read_only_fields = ('author', 'basket',)


# 댓글 CUD
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('basket', 'author',)