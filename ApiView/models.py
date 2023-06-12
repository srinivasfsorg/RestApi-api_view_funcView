from django.db import models

# Create your models here.
class Employs(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=200)
    salary = models.FloatField()
    deptid = models.IntegerField()
