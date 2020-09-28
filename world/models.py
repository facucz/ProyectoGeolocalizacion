from django.db import models
from django.contrib.gis.db.models import PointField


class Blog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    headline = models.CharField(max_length=255)
    point = PointField()

    @property
    def lat_lng(self):
        return list (getattr(self.point, 'coords', [])[::-1])
    
    def __str__(self):
        return self.headline
