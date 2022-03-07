from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname= models.CharField(max_length=20)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    Contact = models.CharField(max_length=15)

    def __str__(self):
        return "%s" %(self.name)

    class Meta:
        db_table = "employee"