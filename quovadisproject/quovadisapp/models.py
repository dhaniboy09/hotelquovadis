from django.contrib.postgres.fields import ArrayField
from django.db import models

from cloudinary.models import CloudinaryField


class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField(default=0)
    services = ArrayField(models.CharField(max_length=100, blank=True))

    def __str__(self):
        return "%s" % (self.name)


class RoomImage(models.Model):
    tag = models.CharField(max_length=100)
    image = CloudinaryField('image')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def primary_image(self, image):
        pass


class SliderImage(models.Model):
    tag = models.CharField(max_length=100)
    image = CloudinaryField('image')
    text = models.CharField(max_length=200, default="Welcome to Quo Vadis")
    sub_text = models.TextField(max_length=300, default="Luxury Boutique Hotel")

    def __str__(self):
        return "%s" % (self.tag)


class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = CloudinaryField('image', default="img/logo.png")

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
