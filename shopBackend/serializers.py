from .models import *
from django.contrib.auth.models import User

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    assoc_item = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    assoc_item = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all())

    class Meta:
        model = Notification
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    added_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    item_comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Item
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    history_user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all())

    class Meta:
        model = Log
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    cart_items = ItemSerializer(many=True, read_only=True)
    history_actions = LogSerializer(many=True, read_only=True)
    # since we will never create user using this serializer
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['cart_items', 'history_actions',
                  'username', 'first_name', 'last_name', 'id']
