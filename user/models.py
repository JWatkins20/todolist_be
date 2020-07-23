from django.db import models
from django.contrib.auth.models import AbstractUser

class todoitem(models.Model):
    description = models.TextField()
    index = models.IntegerField(default=-1)

class user(AbstractUser):
    todolist = models.ManyToManyField(todoitem)
