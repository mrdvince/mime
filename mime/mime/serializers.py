from django.contrib.auth import get_user_model
from rest_framework import serializers

from mime.mime.models import Mime

User = get_user_model()


class MimeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Mime
        fields = ["id", "owner", "no_inf", "inf_name", "city", "estate"]
