from django.urls import path, include 
from .views import PostViewSet, CommentViewSet, FeedView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Posts', PostViewSet)
router.register(r'Comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
]