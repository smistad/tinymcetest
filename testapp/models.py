from django.db import models
from tinymce import models as tinymce_models
from tinymce import widgets

class MyModel(models.Model):
    name = models.CharField(max_length=200)
    sometext = tinymce_models.HTMLField(blank=True)
