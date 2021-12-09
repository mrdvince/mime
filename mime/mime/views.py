from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from mime.mime.models import Mime
from mime.mime.serializers import MimeSerializer
from mime.users.api.serializers import UserSerializer


class MimeList(generics.ListCreateAPIView):
    queryset = Mime.objects.all()
    serializer_class = MimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mime.objects.all()
    serializer_class = MimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


User = get_user_model()


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
