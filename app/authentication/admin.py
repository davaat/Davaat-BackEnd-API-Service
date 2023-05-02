from django.contrib import admin
from .models import User, City


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
admin.site.register(City, CityAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('img', 'phone', 'email', 'updated_on', 'created_on', 'otp_confirmed')
    list_filter = ('otp_confirmed', 'created_on')
    search_fields = ['email', 'firs_name', 'last_name', 'phone']
admin.site.register(User, UserAdmin)
