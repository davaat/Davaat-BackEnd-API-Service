from django.contrib import admin
from .models import Contract, Category, Questionnaire, Question, CustomSettings, GeneralSettings, ContractFile


class ContractFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploader', 'file')
admin.site.register(ContractFile, ContractFileAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
admin.site.register(Category, CategoryAdmin)



class ContractAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'contracting_party', 'updated_on', 'created_on', 'status')
    list_filter = ('updated_on', 'user', 'contracting_party', 'created_on', 'status')
    search_fields = ['title']
admin.site.register(Contract, ContractAdmin)




class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('creator', 'contract')
    list_filter = ("creator", "contract")
    raw_id_fields = ['creator', 'contract']
    inlines = [QuestionInline]

admin.site.register(Questionnaire, QuestionnaireAdmin)



class CustomSettingsAdmin(admin.ModelAdmin):
    list_display = ('contract', 'contract')
admin.site.register(CustomSettings, CustomSettingsAdmin)


class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ('contract', 'contract')
admin.site.register(GeneralSettings, GeneralSettingsAdmin)
