from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from news.models import News, Comment

from rest_framework import generics, status
from django.contrib.auth import get_user_model
from rest_framework import permissions
from django.template.defaultfilters import slugify
from django.utils import timezone
from .permissions import IsCreatorOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CommentSerializer, LatestStorySerializer, UserSerializer, Newserializer, PostSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "stories": reverse("lateststory-list", request=request, format=format),
            "users": reverse("user-list", request=request, format=format),
            "comments": reverse("comment-list", request=request, format=format),
        }
    )


class StoryList(generics.ListCreateAPIView):
    queryset = News.objects.all().order_by("-time")
    serializer_class = LatestStorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["title", "author"]
    filterset_fields = [
        "story_type",
        "author",
        "text",
    ]

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            slug=slugify(self.request.data["title"]),
            time=timezone.now(),
            author=self.request.user.username,
            score=0,
            story_type=self.request.data["story_type"].lower(),
        )


class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = LatestStorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.select_related("story").order_by("-time")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.username, score=0)


class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.select_related("story").order_by("-time")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]
