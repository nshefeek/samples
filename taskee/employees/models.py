from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from organizations.models import Organization, Department, Designation, Role
from django.utils.translation import gettext_lazy as _
from users.models import User, UserManager
# Create your models here.

class Employee(User):

    departments = (
            ('GROCERY', 'Grocery'),
            ('SALES', 'Sales'),
            ('INFORMATION TECHNOLOGY', 'IT'),
            ('ELECTRONICS', 'Electronics'),
            )
        
    designations = (
            ("MANAGER", "Manager"),
            ("SUPERVISOR", "Supervisor"),
            ("COORDINATOR", "Coordinator"),
            ("STAFF", "Staff"),
            )
            
    is_staff = True
    mobile = PhoneNumberField(unique=True, null=False)
    date_of_birth = models.DateField(null=True)
    department = models.CharField(_('Department'), max_length=50, choices=departments, default="SALES")
    designation = models.CharField(_('Designation'), max_length=50, choices=designations, default="STAFF")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    reporting_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    photograph = models.ImageField(blank=True)
    


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Employees'

class Manager(Employee):
    class Meta:
        proxy = True


class Supervisor(Employee):
    class Meta:
        proxy = True

class Coordinator(Employee):
    class Meta:
        proxy = True

class Staff(Employee):
    class Meta:
        proxy = True

