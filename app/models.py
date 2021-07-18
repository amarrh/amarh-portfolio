from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class App(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.title