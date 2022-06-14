from news.models import News, Comment
from django.contrib.auth import get_user_model
from rest_framework import serializers


class LatestStorySerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    author = serializers.ReadOnlyField()
    score = serializers.ReadOnlyField()
    descendants = serializers.ReadOnlyField()
    time = serializers.ReadOnlyField()
    slug = serializers.ReadOnlyField()

    class Meta:
        model = News
        fields = [
            "url",
            "id",
            "title",
            "story_type",
            "author",
            "slug",
            "created_by",
            "time",
            "text",
            "dead",
            "story_url",
            "score",
            "descendants",
        ]


class UserSerializer(serializers.ModelSerializer):
    stories = serializers.HyperlinkedRelatedField(many=True, view_name="user-detail", read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["url", "id", "username", "stories"]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    story = serializers.SlugRelatedField(slug_field="id", queryset=News.objects.all())
    author = serializers.ReadOnlyField()
    score = serializers.ReadOnlyField()
    time = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = [
            "url",
            "id",
            "title",
            "story",
            "author",
            "time",
            "text",
            "dead",
            "comment_url",
            "score",
        ]


class Newserializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    author = serializers.CharField(max_length=255)
    score = serializers.IntegerField(required=False, default=1)
    descendants = serializers.IntegerField(required=False, default=1)
    time = serializers.DateTimeField()
    slug = serializers.SlugField()

    class Meta:
        model = News
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
