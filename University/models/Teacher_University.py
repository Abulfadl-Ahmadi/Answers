from django.db import models
from django.forms import TimeField
from .generator_id import id_generator
from .teacher import Teacher
from university import University

class teacher_university(models.Model):
    ID = models.CharField(primary_key=True, default=id_generator)
    Teacher_ID = Teacher.Teacher_Id
    University_ID = University.University_Id
    Year = models.TimeField(auto_now=False, auto_now_add=False)
    