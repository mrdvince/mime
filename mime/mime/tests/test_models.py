import pytest

from mime.mime.models import Mime
from mime.users.models import User

pytestmark = pytest.mark.django_db


def test_mime_model():
    user = User.objects.create(username="testuser", password="12345")
    mime = Mime.objects.create(user=user, no_inf=1, inf_name="potholes")
    assert mime.inf_name == "potholes"
