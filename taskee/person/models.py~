from django.db import models
from users.models import User
from phonenumber_field.modelfields import PhoneNumberField
from organizations.models import Organization
# Create your models here.

class Person(User):
    #name = models.CharField(max_length=50)
    #email = models.EmailField(max_length=100, unique=True)
    mobile = PhoneNumberField(unique=True, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

