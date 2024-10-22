from rest_framework import serializers
from users.serializers import UserSerializer
from users.models import User


class GenericNotificationRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        data = {"classname": value.__class__.__name__, "id": value.id}
        return data


class NotificationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    sender = UserSerializer(
        User, read_only=True
    )  # The one who executes the notification sending.
    recipient = UserSerializer(User, read_only=True)  # The one who receives the notification.
    unread = serializers.BooleanField(read_only=True)
    verb = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    timestamp = serializers.DateTimeField(read_only=True)
    action_object = GenericNotificationRelatedField(
        read_only=True
    )  # The element related to the notification.


# notify.send(actor, recipient, verb, action_object, target, level, description, public, timestamp, **kwargs)
