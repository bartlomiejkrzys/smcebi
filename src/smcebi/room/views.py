from django.shortcuts import render
from djgeojson.http import HttpJSONResponse
from djgeojson.serializers import Serializer as GeoJSONSerializer
from .models import Room
# Create your views here.

def to_geojson(queryset, properties):

    def wrapper(response):
        serializer = GeoJSONSerializer()
        response = HttpJSONResponse()
        serializer.serialize(
            queryset, stream=response,
            ensure_ascii=False, properties=properties)
        return response
    return wrapper

serialize_properties = (
    'symbol',
    'wing',
    'color',
    'name',
    'geom',
    'popupContent',
)

lowergroundf_geojson = to_geojson(
    Room.lowerground_floor.get_queryset(),
    properties=serialize_properties)

groundf_geojson = to_geojson(
    Room.ground_floor.get_queryset(),
    properties=serialize_properties)

firstf_geojson = to_geojson(
    Room.first_floor.get_queryset(),
    properties=serialize_properties)

secondf_geojson = to_geojson(
    Room.second_floor.get_queryset(),
    properties=serialize_properties)