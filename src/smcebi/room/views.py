from django.shortcuts import render
from djgeojson.http import HttpJSONResponse
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.core.cache import cache
from .models import Room
# Create your views here.

from django.views.decorators.cache import cache_page
serialize_properties = (
    'color',
    'geom',
    'symbol',
    'name',
)

@cache_page(60 * 15)
def geojson_view(request, floor):
    queryset = Room.objects.filter(floor=floor)
    serializer = GeoJSONSerializer()
    response = HttpJSONResponse()
    serializer.serialize(
        queryset, stream=response,
        ensure_ascii=False,
        properties=serialize_properties)
    return response
