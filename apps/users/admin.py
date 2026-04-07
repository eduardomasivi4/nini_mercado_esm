from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_staff', 'is_active')
    list_filter = ('is_admin', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = UserAdmin.fieldsets + (
        ('Extra', {'fields': ('is_admin',)}),
    )