from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'floor')
    list_filter = ('degree', 'sex')
    pass


admin.site.register(Employee, EmployeeAdmin)

