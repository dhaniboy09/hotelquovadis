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
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="images")

    def primary_image(self):
        pass

    def gallery_image(self):
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
    description = models.TextField(max_length=500, default=None, blank=True, null=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu")

    def __str__(self):
        return "%s" % (self.name)
