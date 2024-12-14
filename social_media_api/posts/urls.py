from django import path 
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Posts', PostViewSet)
router.register(r'Comments', CommentViewSet)