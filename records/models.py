from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    matric_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.matric_number} - {self.first_name} {self.last_name}"
