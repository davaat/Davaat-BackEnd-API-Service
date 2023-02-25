from django.contrib import admin
from .models import Reminder



class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'reminder_time', 'remind_model', 'updated_on', 'created_on')
    list_filter = ('updated_on', 'user', 'reminder_time', 'created_on', 'remind_model')
    search_fields = ['title']
admin.site.register(Reminder, ReminderAdmin)
