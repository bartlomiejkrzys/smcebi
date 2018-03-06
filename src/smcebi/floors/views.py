from django.shortcuts import render
import json
from django.views.generic.base import TemplateView
from django.core.serializers.json import DjangoJSONEncoder

from room.models import Room
# Create your views here.

from django.views.decorators.cache import cache_page


class FloorView(TemplateView):
    baselayer_filename = None
    emps_data_url_name = 'emp_geojson'
    rooms_data_url_name = 'rooms_geojson'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(FloorView, self).get_context_data(**kwargs)
        context['folder_name'] = self.fname
        context['floor_no'] = self.floor
        context['room_data_url'] = self.rooms_data_url_name
        context['emps_data_url'] = self.emps_data_url_name
        context['title'] = self.title
        context['x1y1'], context['x1y2'] = self.x1y1, self.x1y2
        context['x2y1'], context['x2y2'] = self.x2y1, self.x2y2
        return context

class LowerGroundFloorView(FloorView):
    title = 'SMCEBI - Lowerground Floor'
    fname = 'lowerground_floor'
    floor = '-1'
    x1y1, x1y2 = [1.60388022712266,4.42028045654297]
    x2y1, x2y2 = [1.5538599350392837,4.256515502929688]
class GroundFloorView(FloorView):
    title = 'SMCEBI - Ground Floor'
    fname = 'ground_floor'
    floor = '0'
    x1y1, x1y2 = [1.6035370388463466,4.609107971191407]
    x2y1, x2y2 = [1.5535167385054869,4.445343017578126]

class FirstFloorView(FloorView):
    x1y1, x1y2 = [1.6031080534200255, 4.794073104858398]
    x2y1, x2y2 = [1.5530877427598309, 4.630308151245118]
    title = 'SMCEBI - First Floor'
    fname = 'first_floor'
    floor = '1'

class SecondFloorView(FloorView):
    x1y1, x1y2 = [1.6044808064677112,4.979467391967774]
    x2y1, x2y2 = [1.554460528839269, 4.815702438354493]
    title = 'SMCEBI - Second Floor'
    fname = 'second_floor'
    floor = '2'

