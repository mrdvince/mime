from rest_framework import generics, permissions

from mime.mime.models import Mime
from mime.mime.serializers import MimeSerializer


class MimeList(generics.ListCreateAPIView):
    """
    List all mimes, or create a new mime.
    """

    queryset = Mime.objects.all()
    serializer_class = MimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


mime_list = MimeList.as_view()


class MimeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a mime instance.
    """

    queryset = Mime.objects.all()
    serializer_class = MimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


mime_detail = MimeDetail.as_view()
