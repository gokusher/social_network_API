from rest_framework import viewsets, permissions
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from authenticate import serializers


User = get_user_model()


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupsSerializer
    permission_classes = [permissions.IsAuthenticated]