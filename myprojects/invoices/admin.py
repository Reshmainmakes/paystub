from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'total_regular_pay', 'total_overtime_pay', 'total_pay')
    search_fields = ('name', 'position')
    list_filter = ('position',)
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'position')
        }),
        ('Pay Information', {
            'fields': ('total_regular_pay', 'total_overtime_pay', 'total_pay'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('total_pay',)  # Example of a read-only field; can be adjusted as needed

admin.site.register(Employee, EmployeeAdmin)
