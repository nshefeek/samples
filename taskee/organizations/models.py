from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=40, null=False)
    
    def __str__(self):
        return self.name + '-' + self.location

class Department(models.Model):
    pass

class Designation(models.Model):
    pass

class Role(models.Model):
    pass