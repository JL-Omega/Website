from django.contrib import admin
from .models import MyUser


class AccountsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active', 'is_admin', 'is_staff',)
    list_editable = ('is_active', 'is_admin', 'is_staff',)


admin.site.register(MyUser, AccountsAdmin)
