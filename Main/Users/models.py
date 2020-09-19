from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUsers(AbstractUser):
    phone = models.CharField(max_length=15)
    sex = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)