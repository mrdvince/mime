"""This module contains the MIME model classes.

Class names include:
- Potholes
- Dumping/Littering
- Accidents
- Flooded roads
- Bad drainages

"""
from django.contrib.auth import get_user_model
from django.db import models

TOWNS = (
    ("nairobi", "Nairobi"),
    ("mombasa", "Mombasa"),
    ("kisumu", "Kisumu"),
    ("eldoret", "Eldoret"),
    ("makindu", "Makindu"),
    ("marsabit", "Marsabit"),
    ("kisii", "Kisii"),
    ("nyamira", "Nyamira"),
    ("migori", "Migori"),
    ("muhanga", "Muhanga"),
    ("nyeri", "Nyeri"),
    ("kiambu", "Kiambu"),
    ("nyandarua", "Nyandarua"),
    ("machakos", "Machakos"),
    ("makueni", "Makueni"),
)

User = get_user_model()


class Mime(models.Model):
    """Default classification model"""

    owner = models.ForeignKey(
        User, related_name="mimes", on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    no_inf = models.PositiveIntegerField(default=1)
    inf_name = models.CharField(max_length=50)
    city = models.CharField(choices=TOWNS, default="nairobi", max_length=50)
    estate = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        :return: name of the classified object
        """
        return self.inf_name
