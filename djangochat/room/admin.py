from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug':('name',)
    }
admin.site.register(Room,RoomAdmin)
