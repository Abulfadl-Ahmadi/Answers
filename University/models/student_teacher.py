from django.db import models
from .generator_id import id_generator
from .student import Student
from .teacher import Teacher


class StudentTeacher(models):
    Id = models.CharField(primary_key=True, default=id_generator)
    Student_Id = Student.Student_Id
    Teacher_Id = Teacher.Teacher_Id
    Year = models.TimeField(auto_now=False, auto_now_add=False)
    Class_Name = models.CharField(max_length=64)
