import os
from django.contrib.gis.utils import LayerMapping
from .models import Room


def run(shp_fpath, mapping, verbose=True):
    try:
        verbose = bool(int(verbose))
    except Exception as err:
        info = 'ERROR: ENV.Verbose={!r:} invalid value. Using default False instead'
        print(info.format(verbose))
        verbose = False

    lm = LayerMapping(Room, shp_fpath, mapping,
                      transform=True, encoding='utf8')

    lm.save(strict=True, verbose=verbose)

def main(verbose):
    room_mapping = {
        'wing' : 'Wing',
        'symbol' : 'Symbol',
        'type' : 'Type',
        'floor' : 'Floor',
        'color': 'Color',
        'name': 'Name',
        'geom' : 'POLYGON',
    }

    for foldername in [
        'lowerground_floor',
        'ground_floor',
        'first_floor',
        'second_floor']:
        print('Loading Room Data for {}'.format(foldername.upper()))
        room_shp_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'data', foldername, 'rooms.shp')
        )
        run(room_shp_path, room_mapping, verbose=verbose)

room_mapping = {
        'wing' : 'Wing',
        'symbol' : 'Symbol',
        'type' : 'Type',
        'floor' : 'Floor',
        'color': 'Color',
        'name': 'Name',
        'geom' : 'POLYGON',
}
def build_path(fname, filename='rooms.shp'):
    return os.path.abspath('.') + '/room/data/{}/{}'.format(fname, filename)

lp = build_path('lower_floor')
gp = build_path('ground_floor')
