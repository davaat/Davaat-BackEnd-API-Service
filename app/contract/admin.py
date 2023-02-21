from django.contrib import admin
from .models import Contract, Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
admin.site.register(Category, CategoryAdmin)



class ContractAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'contracting_party', 'updated_on', 'created_on', 'status')
    list_filter = ('updated_on', 'user', 'contracting_party', 'created_on', 'status')
    search_fields = ['title']
admin.site.register(Contract, ContractAdmin)
