from django.shortcuts import get_object_or_404
from rest_framework import fields, serializers
from django.contrib.auth import get_user_model
from .models import TastingTag, Tastingroom
from accounts.serializers import UserSerializer


# 테이스팅룸 여러개 R
class TastingroomListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'nickname', 'image',)

    class TastingTagSerializer(serializers.ModelSerializer):
        class Meta:
            model = TastingTag
            fields = '__all__'

    participants = UserSerializer(many=True, read_only=True)
    tags = TastingTagSerializer(many=True, read_only=True)

    class Meta:
        model = Tastingroom
        fields = ('id', 'participants', 'tags', 'title',)
        read_only_fields = ('participants', 'tags',)


# movie(movie_img, movie_title), title, tags, participants(개수, 프로필이미지)
# movie, author, participants, name, public, tags
# 테이스팅룸 CRUD
class TastingroomSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'nickname', 'image',)

    class TastingTagSerializer(serializers.ModelSerializer):
        class Meta:
            model = TastingTag
            fields = '__all__'

    participants = UserSerializer(many=True, read_only=True)
    tags = TastingTagSerializer(many=True, read_only=True)

    # Vue에서 보내줄 추가 데이터
    participants_ids = serializers.ListField(write_only=True)
    tags_names = serializers.ListField(write_only=True) # Vue에서 tag의 name을 나눠서 전달 필요

    class Meta:
        model = Tastingroom
        fields = ('movie', 'author', 'participants', 'tags', 'title', 'public', 'participants_ids', 'tags_names',)
        read_only_fields = ('movie', 'author', 'participants', 'tags',)

    def create(self, validated_data):
        participants_ids = validated_data.pop('participants_ids')
        tags_names = validated_data.pop('tags_names')
        tastingroom = Tastingroom.objects.create(**validated_data)
        
        for participants_id in participants_ids:
            participant = get_user_model().objects.get(pk=participants_id)
            tastingroom.participants.add(participant)
        for tags_name in tags_names:
            if TastingTag.objects.filter(name=tags_name).exists():
                tasting_tag = get_object_or_404(TastingTag, name=tags_name)
            else:
                tasting_tag = TastingTag.objects.create(name=tags_name)
            tastingroom.tags.add(tasting_tag)

        return tastingroom

    def update(self, tastingroom, validated_data):
        participants_ids = validated_data.pop('participants_ids')
        tags_names = validated_data.pop('tags_names')
        for attr, value in validated_data.items():
            setattr(tastingroom, attr, value)
        tastingroom.save()

        tastingroom.participants.clear()
        tastingroom.tags.clear()
        
        for participants_id in participants_ids:
            participant = get_user_model().objects.get(pk=participants_id)
            tastingroom.participants.add(participant)
        for tags_name in tags_names:
            if TastingTag.objects.filter(name=tags_name).exists():
                tasting_tag = get_object_or_404(TastingTag, name=tags_name)
            else:
                tasting_tag = TastingTag.objects.create(name=tags_name)
            tastingroom.tags.add(tasting_tag)

        return tastingroom


