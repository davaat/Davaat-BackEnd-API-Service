from django.contrib import admin
from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_on', 'created_on')
    list_filter = ('updated_on', 'created_on')
    search_fields = ['title']
admin.site.register(Contract, ContractAdmin)
