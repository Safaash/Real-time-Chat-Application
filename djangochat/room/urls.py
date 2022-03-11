from django.urls import path
from . import views
urlpatterns = [
    path('',views.rooms,name='rooms'),
    path('<str:slug>',views.room_detail,name='room_detail'),
]
