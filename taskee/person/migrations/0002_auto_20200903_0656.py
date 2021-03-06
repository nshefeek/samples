# Generated by Django 2.2.15 on 2020-09-03 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0001_initial'),
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='person',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='person',
            old_name='dob',
            new_name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='person',
            name='city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='person',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128, region=None, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='person',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
