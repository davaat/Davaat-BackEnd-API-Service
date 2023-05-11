from django.contrib import admin
from .models import User, City, InvitationLink


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
admin.site.register(City, CityAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('img', 'is_company', 'phone', 'email', 'updated_on', 'created_on', 'otp_confirmed')
    list_filter = ('otp_confirmed', 'created_on')
    search_fields = ['email', 'firs_name', 'last_name', 'phone']
    #readonly_fields = ('invitation_referral',)
admin.site.register(User, UserAdmin)


class InvitationLinkAdmin(admin.ModelAdmin):
    list_display = ('invitation_referral', 'unused', 'company', 'created_on')
    list_filter = ('unused', 'created_on', 'company')
    raw_id_fields = ('company'),
admin.site.register(InvitationLink, InvitationLinkAdmin)
