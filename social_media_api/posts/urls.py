from django import path, include 
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Posts', PostViewSet)
router.register(r'Comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]