from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination #implimenting  pagination and filtering
from rest_framework.filters import SearchFilter


class PostPagination(PageNumberPagination):
    page_size = 10
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class= PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


from rest_framework.pagination import PageNumberPagination #implimenting  pagination and filtering

