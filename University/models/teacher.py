from django.db import models
from .generator_id import id_generator
from .enum import *
from .university import University


class Teacher(models.Model):
    Teacher_Id = models.CharField(primary_key=True, default=id_generator)
    Email = models.EmailField(unique=True)
    Tell =  models.CharField(max_length=15)
    F_Name = models.TextField()
    L_Name = models.TextField()
    Major = models.CharField(max_length=1, choices=Major.choices, default=Major.Math)
    Grade = models.CharField(max_length=1, choices=Grade.choices, default=Grade.One)
    Gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.Male)
    NationalCode = models.CharField(max_length=11, unique=True)
