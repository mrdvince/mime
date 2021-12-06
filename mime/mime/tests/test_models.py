import pytest

from mime.mime.models import Location, Mime
from mime.users.models import User

pytestmark = pytest.mark.django_db


def test_mime_model():
    user = User.objects.create(username="testuser", password="12345")
    loc = Location.objects.create(city="test_city", estate="test_state")
    mime = Mime.objects.create(
        user=user, location=loc, no_dumps=1, dumps_name="potholes"
    )
    assert mime.dumps_name == "potholes"
