from django.contrib import admin
from .models import Signature



class SignatureAdmin(admin.ModelAdmin):
    list_display = ('img', 'name', 'user', 'description', 'updated_on', 'created_on')
    list_filter = ('updated_on', 'user')
    search_fields = ['title']
admin.site.register(Signature, SignatureAdmin)
