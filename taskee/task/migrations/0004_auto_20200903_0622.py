# Generated by Django 2.2.15 on 2020-09-03 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20200903_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
