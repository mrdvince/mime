"""One url file to rule them all.

Behold the power of the "root" urls.py file. 😂😂

Disclaimer: don't do this (or do).
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from mime.mime import views as mime_views
from mime.users.api import views as user_views

app_name = "api"
# Definetly better ways to do this, but this is a quick and dirty way
# to get the app running. Will use Default Router in the later.
user_list = user_views.UserViewSet.as_view(
    {
        "get": "list",
    }
)
user_detail = user_views.UserViewSet.as_view(
    {
        "get": "retrive",
    }
)
urlpatterns = [
    path("users/", user_list),
    path("users/<int:pk>/", user_detail),
]

# concat the urlpatterns
urlpatterns += [
    path("mime/", mime_views.mime_list, name="mime-list"),
    path("mime/<int:pk>/", mime_views.mime_detail, name="mime-detail"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
