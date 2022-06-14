from rest_framework import serializers
from django.contrib.auth.models import User

from core.models import Post, Like


class UserSerializer(serializers.ModelSerializer):
    post_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    like_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'post_set', 'like_set']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    like_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'user', 'like_set']


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']
