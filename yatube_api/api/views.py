from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins
from rest_framework import filters

from posts.models import Group, Post
from .serializers import (
    CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer
)
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Запись в поле 'author' текущего пользователя при сохранении."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        """Запрос из базы данных комментариев к указанному посту."""
        post_id = self.kwargs.get('post_id')
        comment_post = get_object_or_404(Post, id=post_id)
        return comment_post.comments

    def perform_create(self, serializer):
        """Запись в поле 'post' указанного поста при сохранении."""
        post_id = self.kwargs.get('post_id')
        comment_post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=comment_post)


class CreateListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass


class FollowViewSet(CreateListViewSet):

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Запрос из базы данных подписок текущего пользователя."""
        return self.request.user.followings

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
