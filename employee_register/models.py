from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    firstname= models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    Contact = models.CharField(max_length=20)

    def __str__(self):
        return "%s" %(self.firstname)

    class Meta:
        db_table = "employee"