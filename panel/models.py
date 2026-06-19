from django.db import models
from django.contrib.auth.models import User

class Server(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(max_length=16)
    password = models.CharField(max_length=160)
    port = models.IntegerField()