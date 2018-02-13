from django.shortcuts import render
from djgeojson.http import HttpJSONResponse
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.core.cache import cache
from .models import Room
# Create your views here.

serialize_properties = (
    'color',
    'geom',
    'popupContent',
)


def geojson_view(request, floor):
    queryset = Room.objects.filter(floor=floor)
    serializer = GeoJSONSerializer()
    response = HttpJSONResponse()
    serializer.serialize(
        queryset, stream=response,
        ensure_ascii=False,
        properties=serialize_properties)
    return response
