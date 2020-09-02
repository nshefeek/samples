from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Employee
from .forms import RegistrationForm 


class EmployeeAdmin(BaseUserAdmin):
    form = RegistrationForm

    list_display = ('email', 'name', 'mobile', 'date_of_birth', 'organization', 'designation', 'is_staff',  'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('name', 'mobile', 'date_of_birth', 'photograph')}),
        ('Organization info', {'fields': ('organization', 'department', 'designation', 'reporting_to', 'is_active', 'last_login', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'mobile', 'date_of_birth', 'photograph')}),
        ('Organizationl info', {'fields': ('organization', 'department', 'designation', 'reporting_to', 'is_active', 'last_login', 'date_joined')}),

        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name', 'mobile')
    ordering = ('email', 'name')
    filter_horizontal = ()


admin.site.register(Employee, EmployeeAdmin)
