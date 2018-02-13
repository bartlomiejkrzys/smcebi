import os

from django.contrib.gis.utils import LayerMapping

from .models import Employee


def run(shp_fpath, mapping, verbose=True):
    try:
        verbose = bool(int(verbose))
    except Exception as err:
        info = 'ERROR: ENV.Verbose={!r:} invalid value. Using default False instead'
        print(info.format(verbose))
        verbose = False

    lm = LayerMapping(Employee, shp_fpath, mapping,
                      transform=False, encoding='utf8')

    lm.save(strict=True, verbose=verbose)

def main(verbose):
    employee_mapping = {
        'name' : 'Name',
        'degree' : 'Degree',
        'surname' : 'Surname',
        'sex' : 'Sex',
        'roomid' : 'RoomID',
        'email' : 'Email',
        'url' : 'Url',
        'phone' : 'Phone',
        'position' : 'Position',
        'floor': 'Floor',
        'geom' : 'POINT',
    }

    for foldername in [
        'lowerground_floor',
        'ground_floor',
        'first_floor',
        'second_floor']:
        print('Loading Employee Data for {}'.format(foldername.upper()))
        emp_shp_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'data', foldername, 'employees.shp')
        )
        run(emp_shp_path, employee_mapping, verbose=verbose)
