from email.headerregistry import Address
from django.db import models
from .generator_id import id_generator
from .enum import Gender


class University(models.Model):
    University_Id = models.CharField(primary_key=True, default=id_generator)
    Name = models.TextField()
    Tell = models.CharField(max_length=15)
    Address = models.TextField()
    Capacity = models.CharField(max_length=3)
    Headmaster = models.CharField(max_length=128)
    Gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.Male)