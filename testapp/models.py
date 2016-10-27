from django.db import models
from tinymce import models as tinymce_models

class MyModel(models.Model):
    name = models.CharField(max_length=200)
    sometext = tinymce_models.HTMLField()
