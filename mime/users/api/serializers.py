from django.contrib.auth import get_user_model
from rest_framework import serializers

from mime.mime.models import Mime

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model (used for the API)
    """

    mime = serializers.PrimaryKeyRelatedField(many=True, queryset=Mime.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "mime"]
