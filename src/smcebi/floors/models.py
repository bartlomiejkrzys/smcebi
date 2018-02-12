from django.db import models

# Create your models here.
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class LowerGroundFloor(models.Model):
    floor = models.IntegerField()
    geom = models.LineStringField(srid=3857)

# Auto-generated `LayerMapping` dictionary for LowerGroundFloor model
lowergroundfloor_mapping = {
    'floor' : 'Floor',
    'geom' : 'LINESTRING',
}
