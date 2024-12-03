from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    marks = models.IntegerField()
    class Meta:
        db_table = 'student'

class Address(models.Model):
    class Meta:
        db_table = 'address'
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='addresslist')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)


