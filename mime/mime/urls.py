from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from mime.mime import views

urlpatterns = [
    path("mime/", views.mime_list),
    path("mime/<int:pk>/", views.mime_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
