# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models
from room.models import Room

class Employee(models.Model):
    name = models.CharField(max_length=15)
    degree = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE,
        null=True)
    email = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=50)
    floor = models.IntegerField()
    geom = models.PointField(srid=4326)

    def __repr__(self):
        return '{cls}<Name={name} Surname={surname}>'.format(
            cls=self.__class__.__name__,
            name=self.name,
            surname=self.surname
    )

    def __str__(self):
        template = '{title} {name} {surname}'
        return template.format(
            title=self.degree,
            name=self.name,
            surname=self.surname
        )
