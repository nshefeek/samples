# Generated by Django 2.2.15 on 2020-09-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
