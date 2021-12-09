from django.contrib.auth import get_user_model
from rest_framework import viewsets

from mime.users.api.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Readonly viewset for the User model
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
