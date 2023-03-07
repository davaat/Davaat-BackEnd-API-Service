from django.db import models
from django.db.models import Model
from authentication.models import User



class Subscription(Model):
    title = models.CharField(max_length=256, unique=True)
    price = models.CharField(max_length=256)
    signature_number = models.IntegerField()
    contract_number = models.IntegerField()
    duration_day = models.IntegerField()

    def __str__(self):
        return str(self.title)


class UserSubscription(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='Subscription')
    start_date = models.CharField(max_length=256)
    end_date = models.CharField(max_length=256)
    CHOICES = (('فعال', 'فعال'),('به اتمام رسیده', 'به اتمام رسیده'),('لغو شده', 'لغو شده'))
    status = models.CharField(max_length=256, choices=CHOICES, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.subscription.title) +'|'+ str(self.user)
