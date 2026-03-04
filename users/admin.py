from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """
    Admin interface for the custom User model
    - Adds the 'role' field to forms and display
    - Keeps default Django User functionality
    """
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Role & Audit Info", {"fields": ("role", "created_at", "updated_at")}),
    )

    # Fields that are visible but not editable
    readonly_fields = ("created_at", "updated_at")

    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        ("Role", {"fields": ("role",)}),
    )
    list_display = ("username", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)