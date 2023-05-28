from django.db import models

# tag model
class Tag(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return str(self.name)
