from django.db import models
from django.db.models import Model


class Contract(Model):
    title = models.CharField(max_length=256)
    body = models.TextField(max_length=1000)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
