# Generated by Django 2.2.15 on 2020-09-03 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
        ('employees', '0002_auto_20200902_0738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('CRITICAL', 'Critical'), ('MAJOR', 'Major'), ('MEDIUM', 'Medium'), ('MINOR', 'Minor')], default='MEDIUM', max_length=30, verbose_name='Priority')),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('ASSIGNED', 'Assigned'), ('ACKNOWLEDGED', 'Acknowledged'), ('WAITING', 'Waiting'), ('COMPLETED', 'Completed'), ('INCOMPLETE', 'Incomplete')], default='CREATED', max_length=10, verbose_name='Status')),
                ('assigned_designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Designation')),
                ('assigned_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Department')),
                ('assigned_organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizations.Organization')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
        ),
    ]
