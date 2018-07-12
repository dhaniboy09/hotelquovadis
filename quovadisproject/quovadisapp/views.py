from django.shortcuts import render, get_object_or_404
from .models import SliderImage, Activity, Service, Room


# Create your views here.


def index(request):
    images = SliderImage.objects.all()
    main_image = None
    for image in images:
        if image.tag == 'main':
            main_image = image
            images = SliderImage.objects.exclude(tag='main')
            break

    context = {
        "main_image": main_image,
        "secondary_images": images
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
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, 'quovadisapp/rooms.html', context)


def room_detail(request, room_id):
    return render(request, 'quovadisapp/detail.html')


def restaurant(request):
    return render(request, 'quovadisapp/restaurant.html')


def contact(request):
    return render(request, 'quovadisapp/contact.html')


