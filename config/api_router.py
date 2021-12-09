from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from mime.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"users", UserViewSet)
# router.register(r"mimes", MimeViewSet)

app_name = "api"
urlpatterns = router.urls
