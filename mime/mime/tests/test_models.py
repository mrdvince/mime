import pytest

from mime.mime.models import Mime

pytestmark = pytest.mark.django_db


def test_mime_model():
    """Test mime model."""
    mime = Mime.objects.create(no_inf=1, inf_name="potholes")
    assert mime.inf_name == "potholes"
