from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView
from django.views.generic import TemplateView

import employee.views

urlpatterns = [
    url(r'^geojson/(?P<floor>-*\d)/$', employee.views.geojson_view, name='emp_geojson'),
]