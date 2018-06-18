from django.contrib import admin
from .models import Room, RoomImage, Activity, Service, Category, MenuItem

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(Activity)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(MenuItem)
