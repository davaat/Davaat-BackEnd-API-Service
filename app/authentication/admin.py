from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('img', 'phone', 'email', 'updated_on', 'created_on', 'otp_confirmed', 'email_confirmed', 'is_driver')
    list_filter = ('email_confirmed', 'otp_confirmed', 'created_on', 'is_driver')
    search_fields = ['email', 'firs_name', 'last_name', 'phone']
admin.site.register(User, UserAdmin)
