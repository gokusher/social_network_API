from rest_framework import viewsets, permissions 

from . import serializers
from . import permissions as custom_permissions
from .models import (GroupModel, PostModel, CommentModel,
                     FollowModel, LikesModel)


class BaseViewSet(viewsets.ModelViewSet):
    """"""
    def get_permissions(self):
        """Custom permissions mixin
        """
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [custom_permissions.IsAuthor]
        return [permission() for permission in permission_classes]
    

class GroupViewSet(BaseViewSet):
    queryset = GroupModel.objects.all()
    serializer_class = serializers.GroupSerializer


class PostViewSet(BaseViewSet):
    queryset = PostModel.objects.all()
    serializer_class = serializers.PostSerializer
    

class CommentViewSet(BaseViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = serializers.CommentSerializer


class FollowViewSet(BaseViewSet):
    queryset = FollowModel.objects.all()
    serializer_class = serializers.FollowSerializer


class LikesViewSet(BaseViewSet):
    queryset = LikesModel.objects.all()
    serializer_class = serializers.LikesSerializer
