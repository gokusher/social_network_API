from rest_framework import serializers
from django.contrib.auth.models import User

from . import models


ALL_FIELDS = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupModel
        fields = ALL_FIELDS


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostModel
        fields = ALL_FIELDS


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentModel
        fields = ALL_FIELDS


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FollowModel
        fields = ALL_FIELDS


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LikesModel
        fields = ALL_FIELDS