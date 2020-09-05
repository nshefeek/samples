from django.db import models
from employees.models import Employee
from organizations.models import Organization, Department, Designation
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Task(models.Model):

    statuses = (
            ('CREATED', 'Created'),
            ('ASSIGNED', 'Assigned'),
            ('ACKNOWLEDGED', 'Acknowledged'),
            ('WAITING', 'Waiting'),
            ('COMPLETED', 'Completed'),
            ('INCOMPLETE', 'Incomplete'),
            )
    priorities = (
            ('CRITICAL', 'Critical'),
            ('MAJOR', 'Major'),
            ('MEDIUM', 'Medium'),
            ('MINOR', 'Minor'),
            )

    task_id = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    priority = models.CharField(_('Priority'), max_length=30, choices=priorities, default='MEDIUM')
    status = models.CharField(_('Status'), max_length=10, choices=statuses, default='CREATED')
    #assigned_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    assigned_group = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    attachment = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.task_id

    def save(self, *args, **kwargs):
        self.task_id = 'TSK' + str(self.id)
        super(Task, self).save(*args, **kwargs)
         

