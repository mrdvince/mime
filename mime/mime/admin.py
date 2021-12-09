from django.contrib import admin

from mime.mime.models import Mime

# Regiter mime model in admin.
admin.site.register(Mime)
