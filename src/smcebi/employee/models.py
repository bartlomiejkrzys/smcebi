# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Employee(models.Model):
    name = models.CharField(max_length=15)
    degree = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    roomid = models.IntegerField()
    email = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=50)
    floor = models.IntegerField()
    geom = models.PointField(srid=4326)

    def __str__(self):
        template = '{title} {name} {surname}'
        return template.format(
            title=self.degree,
            name=self.name,
            surname=self.surname
        )

    def to_dict(self):
        return {
            'Name': ' '.join((self.name, self.surname)),
            'Degree': self.degree,
            'Position': self.position,
            'Email': self.email,
            'Phone': self.phone,
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
        url_tag = '<tr><th scope="row">URL<td><a href={}>{}</a></td></tr>'
        table_insides += url_tag.format(self.url, self.url)
        return '<table>' + ''.join(table_insides) + '</table>'
