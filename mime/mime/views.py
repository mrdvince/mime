from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from rest_framework import generics, permissions

from mime.mime.models import Mime
from mime.mime.run import get_prediction
from mime.mime.serializers import MimeSerializer

from .forms import ImageUploadForm


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


# Django view, the rest framerwork view to be refactored later (moved to api module)
class Run(LoginRequiredMixin, generic.CreateView):
    """Run the model
    Store the inference result and image path in the database
    """

    model = Mime
    form_class = ImageUploadForm
    template_name = "mime/run.html"

    def form_valid(self, form):
        mime = form.save(commit=False)
        mime.owner = self.request.user
        image = form.cleaned_data["upload"]
        image_bytes = image.file.read()
        mime.inf_name = get_prediction(image_bytes)

        mime.save()

        return HttpResponseRedirect(
            reverse("users:detail", args=(self.request.user.username,))
        )


run = Run.as_view()
