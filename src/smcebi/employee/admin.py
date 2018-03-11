from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Employee

class EmployeeAdmin(LeafletGeoAdmin):
    list_display = ('name', 'surname', 'floor')
    list_filter = ('degree', 'sex')
    pass


admin.site.register(Employee, EmployeeAdmin)

