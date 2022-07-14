from django.db import models

# Create your models here.

class Employee_details(models.Model):
    name = models.CharField(max_length=20)
    emp_id = models.IntegerField()
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.name



