from django.db import models
from django import forms
from .generator_id import id_generator

from .enum import Grade, Gender


class Student(models.Model):
    ID = models.CharField(primary_key=True, default=id_generator)
    Student_id = models.CharField(max_length=11, unique=True)
    Username = models.CharField(max_length=200, unique=True)
    PassWord = forms.CharField(widget=forms.PasswordInput)
    Email = models.EmailField(unique=True)
    FirstName = models.TextField()
    LastName = models.TextField()
    NationalCode = models.CharField(max_length=11, unique=True)
    Gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.Male)
    Grade = models.CharField(max_length=10, choices=Grade.choices, default=Grade.Freshman)
    Created_at = models.DateTimeField(auto_now_add=True)
