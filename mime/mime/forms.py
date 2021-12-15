from django import forms

from mime.mime.models import Mime


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Mime
        fields = ["city", "estate", "upload"]
