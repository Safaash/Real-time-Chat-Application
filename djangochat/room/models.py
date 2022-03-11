from django.db import models
from django.contrib.auth.models import User
class Room(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    content=models.TextField()

    class Meta:
        ordering=('time',)
    def __str__(self) -> str:
        return self.user.username
