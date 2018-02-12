from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Room

class RoomAdmin(LeafletGeoAdmin):
    modifiable = False


admin.site.register(Room, RoomAdmin)

