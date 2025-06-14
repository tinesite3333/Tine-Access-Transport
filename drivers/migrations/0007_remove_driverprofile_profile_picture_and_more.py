# Generated by Django 5.2.1 on 2025-06-01 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0006_driverprofile_driver_license_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driverprofile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='driverprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='driver_profiles/'),
        ),
        migrations.AlterField(
            model_name='driverprofile',
            name='driver_license',
            field=models.ImageField(blank=True, null=True, upload_to='driver_license/'),
        ),
    ]
