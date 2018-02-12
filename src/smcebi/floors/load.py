import os
from django.contrib.gis.utils import LayerMapping
from .models import LowerGroundFloor
from .floordata import geojson

for feat in geojson['features']:
    geom = feat['properties']['geometry']
    lg = LowerGroundFloor(geom=geom, floor=-1)
    lg.save()


room_mapping = {
     'floor' : 'Floor',
     'geom' : 'LINESTRING',
}
przyziemie_room_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'baselayer.shp'))

def run(verbose=True):
    try:
        verbose = bool(int(verbose))
    except Exception as err:
        info = 'ERROR: ENV.Verbose={!r:} invalid value. Using default False instead'
        print(info.format(verbose))
        verbose = False

    lm = LayerMapping(LowerGroundFloor, przyziemie_room_shp, room_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)

