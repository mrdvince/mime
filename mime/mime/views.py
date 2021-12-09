from rest_framework import generics

from mime.mime.models import Mime
from mime.mime.serializers import MimeSerializer


class MimeList(generics.ListCreateAPIView):
    queryset = Mime.objects.all()
    serializer_class = MimeSerializer


class MimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mime.objects.all()
    serializer_class = MimeSerializer
