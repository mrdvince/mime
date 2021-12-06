"""
[mime models]
id: uuid
user_id => FK->user.id
name: str
created at: dt
no_dumps: int -> objects found in photo
dumps_name: str -> single name currently since this is a classification model
location of dumpsite -> [city and estate]
"""

import uuid

from django.conf import settings
from django.db import models


class Location(models.Model):
    """Location model

    Model used to store the mime location details
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(max_length=50)
    estate = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.city + ", " + self.estate if self.estate else self.city


class Mime(models.Model):
    """Default classification model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    # Calling it dumps, can't figure out a name to group the classes to
    no_dumps = models.PositiveIntegerField(default=1)
    dumps_name = models.CharField(max_length=50)

    def __str__(self):
        """Class names include:
        - Potholes
        - Dumping/Littering
        - Accidents
        - Flooded roads
        - Bad drainages

        :return: name of the classified object
        """
        return self.dumps_name
