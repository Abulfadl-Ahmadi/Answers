from django.db import models


class Gender(models.TextChoices):
    Female = "F", "Female"
    Male = "M", "Male"


class Grade(models.TextChoices):
    One = "1", "1"
    Two = "2", "2"
    Three = "3", "3"
    Four = "4", "4"
    Five = "5", "5"
    Six = "6", "6"
    Seven = "7", "7"
    Eight = "8", "8"
    Nine = "9", "9"

class Major(models.TextChoices):
    Math = 'M', "Math"
    physic = 'P', 'Physic'
    Geograpy = 'G' 'Geograpy'
    Religious = 'R', 'Religious'
    Chemistry = 'C', 'Chemistry'
    Arabic = 'A', 'Arabic'
    English = 'E', 'English'
    
