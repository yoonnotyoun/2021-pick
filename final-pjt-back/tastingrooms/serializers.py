from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import TastingTag, Tastingroom
from accounts.serializers import UserSerializer



class TastingTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TastingTag
        fields = '__all__'



# movie(movie_img, movie_title), title, tags, participants(개수, 프로필이미지)
# movie, author, participants, name, public, tags
class TastingroomSerializer(serializers.ModelSerializer):

    participants = UserSerializer(many=True)
    tags = TastingTagSerializer(many=True)

    class Meta:
        model = Tastingroom
        fields = '__all__'
        read_only_fields = ('movie', 'author', 'participants', 'tags',)


class TastingroomListSerializer(serializers.ModelSerializer):

    participants = UserSerializer(many=True)

    class Meta:
        model = Tastingroom
        fields = ('id', 'participants', 'title',)
        read_only_fields = ('participants',)