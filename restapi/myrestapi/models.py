from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=60)
    esal=models.IntegerField()
    eadd=models.CharField(max_length=60)
    