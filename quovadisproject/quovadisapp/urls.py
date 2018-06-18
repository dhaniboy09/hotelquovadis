from django.urls import path
from . import views

app_name = 'quovadisapp'
urlpatterns = [
    path('about/', views.about, name='about'),
    path('activities/', views.activities, name='activities'),
    path('contact/', views.contact, name='contact'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('restaurant/', views.restaurant, name='restaurant'),
]
