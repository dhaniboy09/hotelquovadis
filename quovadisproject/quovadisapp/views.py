from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'quovadisapp/index.html')


def rooms(request):
    return render(request, 'quovadisapp/rooms.html')


def room_detail(request, room_id):
    return render(request, 'quovadisapp/detail.html')


def restaurant(request):
    return render(request, 'quovadisapp/restaurant.html')


def contact(request):
    return render(request, 'quovadisapp/contact.html')


def about(request):
    return render(request, 'quovadisapp/about.html')


def activities(request):
    return render(request, 'quovadisapp/activities.html')
