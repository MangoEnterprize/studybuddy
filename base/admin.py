from django.contrib import admin

# Register your models here.
#add room model from models.py
from .models import Room, Topic, Message, User

# make viewable from admin panel
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)