from django.contrib.gis.db import models


class LGFloorManager(models.Manager):
    def get_queryset(self):
        return super(LGFloorManager, self).get_queryset().filter(floor=-1)


class GFloorManager(models.Manager):
    def get_queryset(self):
        return super(GFloorManager, self).get_queryset().filter(floor=0)


class FFloorManager(models.Manager):
    def get_queryset(self):
        return super(FFloorManager, self).get_queryset().filter(floor=1)


class SFloorManager(models.Manager):
    def get_queryset(self):
        return super(SFloorManager, self).get_queryset().filter(floor=2)


class Room(models.Model):
    wing = models.CharField(max_length=3)
    symbol = models.CharField(max_length=30)
    type = models.CharField(max_length=50)
    floor = models.IntegerField()
    color = models.CharField(max_length=10)
    name = models.CharField(max_length=250)
    geom = models.PolygonField(srid=4326)

    def to_dict(self):
        return {
            'Symbol': self.symbol,
            'Name': self.name,
        }

    @property
    def popupContent(self):
        row_temp = '<tr>\
            <th scope="row">{property_name}</th>\
            <td>{property_value}</td>\
            </tr>'
        table_insides = [row_temp.format(
            property_name=name,
            property_value=value
        ) for (name, value) in self.to_dict().items()]
        return '<table>' + ''.join(table_insides) + '</table>'

    def __repr__(self):
        return '{cls}<Symbol={symbol} Wing={wing}>'.format(
            cls=self.__class__.__name__,
            wing=self.wing,
            symbol=self.symbol,
        )

    def __str__(self):
        return 'Room {}'.format(self.symbol)