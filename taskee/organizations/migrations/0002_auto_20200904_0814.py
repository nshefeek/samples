# Generated by Django 2.2.15 on 2020-09-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='organization_id',
            field=models.CharField(default=0, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='qr_code',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
