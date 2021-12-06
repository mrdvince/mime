"""
[mime models]
id: uuid
user_id => FK->user.id
name: str
created at: dt
no_dumps: int -> objects found in photo
dumps_name: str -> single name currently since this is a classification model
location of dumpsite -> [city and location]
"""

import uuid

from django.conf import settings
from django.db import models


class Mime(models.Model):
    """Default classification model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # Calling it dumps, can't figure out a name to group the classes to
    no_dumps = models.IntegerField()
    dumps_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        """Class names include:
        - Potholes
        - Dumping/Littering
        - Accidents
        - Flooded roads
        - Bad drainages

        :return: name of the classified object
        """
        return self.name
