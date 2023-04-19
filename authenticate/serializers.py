from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


User = get_user_model()


# Serializers define the API representation.
class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']