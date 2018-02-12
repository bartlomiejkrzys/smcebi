from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class FloorView(TemplateView):
    baselayer_filename = None
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(FloorView, self).get_context_data(**kwargs)
        context['folder_name'] = self.fname
        context['room_data'] = self.room_data_url_name
        context['title'] = self.title
        context['x1y1'], context['x1y2'] = self.x1y1, self.x1y2
        context['x2y1'], context['x2y2'] = self.x2y1, self.x2y2
        return context

class LowerGroundFloorView(FloorView):
    title = 'SMCEBI - Lowerground Floor'
    fname = 'lowerground_floor'
    room_data_url_name = 'lowerground_rooms'
    x1y1, x1y2 = [1.6180366932206667,4.503536224365235]
    x2y1, x2y2 = [1.51799559802871,4.176006317138673]

class GroundFloorView(FloorView):
    x1y1, x1y2 = [1.622841289603995,4.695453643798829]
    x2y1, x2y2 = [1.5121611516421967,4.3679237365722665]
    title = 'SMCEBI - Ground Floor'
    fname = 'ground_floor'
    room_data_url_name = 'ground_rooms'

class FirstFloorView(FloorView):
    x1y1, x1y2 = [1.6224981045261873, 4.872608184814454]
    x2y1, x2y2 = [1.511817948424566, 4.5450782775878915]
    title = 'SMCEBI - First Floor'
    fname = 'first_floor'
    room_data_url_name = 'first_rooms'

class SecondFloorView(FloorView):
    x1y1, x1y2 = [1.6212969562954151,5.05645751953125]
    x2y1, x2y2 = [1.510616736735647, 4.7289276123046875]
    title = 'SMCEBI - Second Floor'
    fname = 'second_floor'
    room_data_url_name = 'second_rooms'

