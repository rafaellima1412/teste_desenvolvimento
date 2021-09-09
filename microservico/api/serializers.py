from microservico.models import Actions, Message, User
from rest_framework import serializers


class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = ("like", "unlike", "message_id")


class UserSerializer(serializers.ModelSerializer):
    message = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("name", "message")


class MessageSerializer(serializers.ModelSerializer):
    like = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Message
        fields = ("user_id", "destination_user_id", "message", "like")
