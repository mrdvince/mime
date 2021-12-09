from django.contrib.auth import get_user_model
from rest_framework import serializers

from mime.mime.models import Mime

User = get_user_model()


class MimeSerializer(serializers.ModelSerializer):
    mime = serializers.PrimaryKeyRelatedField(many=True, queryset=Mime.objects.all())

    class Meta:
        model = Mime
        fields = ["id", "username", "mime"]
