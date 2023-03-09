from django.contrib import admin
from .models import Subscription, UserSubscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'signature_number', 'contract_number', 'duration_day')
admin.site.register(Subscription, SubscriptionAdmin)


class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'start_date')
admin.site.register(UserSubscription, UserSubscriptionAdmin)
