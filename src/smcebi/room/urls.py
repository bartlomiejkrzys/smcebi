from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView
from django.views.generic import TemplateView

import room.views
from room.models import Room

urlpatterns = [
    url(r'^geojson/(?P<floor>-*\d)$', room.views.geojson_view, name='rooms_geojson'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
]