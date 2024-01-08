from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.


class CustomerUser(User):
    mobile = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=120,  null=True, blank=True)


    def __str__(self):
        return self.username






