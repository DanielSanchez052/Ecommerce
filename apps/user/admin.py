from django.contrib import admin

from apps.user.models import User
from apps.orders.admin import AddressInLine

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('username, email','name')
    list_display = ("id", "username", "email", "name", "last_name", "cellPhone", "is_staff", "is_superuser","last_login","is_active")
    inlines = [
        AddressInLine
    ]
    ordering = ['is_active']