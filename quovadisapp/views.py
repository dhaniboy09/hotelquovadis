from django.shortcuts import render, get_object_or_404
from .models import SliderImage, Activity, Service, Room, Category


# Create your views here.


def index(request):
    images = SliderImage.objects.all()
    main_image = None
    for image in images:
        if image.tag == 'main':
            main_image = image
            images = SliderImage.objects.exclude(tag='main')
            break

    room_info = {}
    rooms = Room.objects.all()
    for room in rooms[:3]:
        room_info[room.name] = [room, room.images.all()[0]]

    context = {
        "main_image": main_image,
        "secondary_images": images,
        "room_info": room_info
    }
    return render(request, 'quovadisapp/index.html', context)


def about(request):
    services = Service.objects.all()
    if len(services) > 8:
        services = services[:8]

    context = {"services": services}

    return render(request, 'quovadisapp/about.html', context)


def activities(request):
    activities = Activity.objects.all()
    context = {"activities": activities}
    return render(request, 'quovadisapp/activities.html', context)


def rooms(request):
    room_info = {}
    rooms = Room.objects.all()
    for room in rooms:
        room_info[room.name] = [room, room.images.all()]
    context = {"room_info": room_info}
    return render(request, 'quovadisapp/rooms.html', context)


def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    room_info = [room, room.images.all()]
    context = {"room_info": room_info}
    return render(request, 'quovadisapp/detail.html', context)


def restaurant(request):
    breakfast = []
    lunch = []
    dinner = []
    categories = Category.objects.all()
    for category in categories:
        if category.name == "Breakfast":
            breakfast = category.menu.all()
        elif category.name == "Lunch":
            lunch = category.menu.all()
        elif category.name == "Dinner":
            dinner = category.menu.all()

    context = {"breakfast": breakfast, "lunch": lunch, "dinner": dinner}
    return render(request, 'quovadisapp/restaurant.html', context)


def contact(request):
    return render(request, 'quovadisapp/contact.html')


