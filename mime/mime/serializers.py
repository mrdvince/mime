from django.contrib.auth import get_user_model
from rest_framework import serializers

from mime.mime.models import Mime

User = get_user_model()


class MimeSerializer(serializers.ModelSerializer):
    """Mime serializer"""

    # Attach user to mime
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        """
        Meta class for Mime serializer
        """

        model = Mime
        fields = ["id", "owner", "no_inf", "inf_name", "city", "estate"]
