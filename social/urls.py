from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'group', views.GroupViewSet)
router.register(r'post', views.PostViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'follow', views.FollowViewSet)
router.register(r'likes', views.LikesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]