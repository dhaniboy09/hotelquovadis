from django.contrib.postgres.fields import ArrayField
from django.db import models

from cloudinary.models import CloudinaryField


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField(default=0)
    services = ArrayField(models.CharField(max_length=100, blank=True))
    primary_image = CloudinaryField('image')

    def __str__(self):
        return "%s" % (self.name)


class RoomImage(models.Model):
    image = CloudinaryField('image')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = CloudinaryField('image')

    def __str__(self):
        return "%s" % (self.name)


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return "%s" % (self.name)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField(default=0)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)
