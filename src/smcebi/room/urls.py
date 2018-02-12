from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView
from django.views.generic import TemplateView

import room.views
from room.models import Room

urlpatterns = [
    url(r'^lowergroundf.geojson$', room.views.lowergroundf_geojson, name='lowerground_rooms'),
    url(r'^groundf.geojson$', room.views.groundf_geojson, name='ground_rooms'),
    url(r'^firstf.geojson$', room.views.firstf_geojson, name='first_rooms'),
    url(r'^secondf.geojson$', room.views.secondf_geojson, name='second_rooms'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^home2$', TemplateView.as_view(template_name='index2.html'), name='home2'),
    url(r'^home3$', TemplateView.as_view(template_name='index3.html'), name='home3'),
]