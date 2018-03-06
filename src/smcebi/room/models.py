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
    search = models.CharField(max_length=50)
    geom = models.PolygonField(srid=4326)

    def __repr__(self):
        return '{cls}<Symbol={symbol} Wing={wing}>'.format(
            cls=self.__class__.__name__,
            wing=self.wing,
            symbol=self.symbol,
        )

    def __str__(self):
        return 'Room {}'.format(self.symbol)