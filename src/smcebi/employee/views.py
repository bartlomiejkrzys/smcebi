from django.shortcuts import render
from djgeojson.serializers import Serializer as GeoJSONSerializer
from djgeojson.http import HttpJSONResponse
# Create your views here.
from .models import Employee


serialize_properties = (
    'geom',
    'sex',
    'name',
    'surname',
    'phone',
    'email',
    'degree',
    'url',
    'search'
)

def geojson_view(request, floor):
    queryset = Employee.objects.filter(floor=floor)
    serializer = GeoJSONSerializer()
    response = HttpJSONResponse()
    serializer.serialize(
        queryset, stream=response,
        ensure_ascii=False,
        properties=serialize_properties)
    return response
