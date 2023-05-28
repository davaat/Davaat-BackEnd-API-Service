from django.db import models
from authentication.models import User

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reminder_user')
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=1000, null=True, blank=True)
    reminder_time = models.CharField(max_length=256)
    CHOICES = (('یک روز قبل', 'یک روز قبل'),
               ('دو روز قبل', 'دو روز قبل'),
               ('سه روز قبل', 'سه روز قبل'),
               ('یک هفته قبل', 'یک هفته قبل'))
    remind_model = models.CharField(max_length=256, choices=CHOICES, default='یک روز قبل')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
