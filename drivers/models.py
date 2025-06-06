from django.db import models
from django.conf import settings

class DriverProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='driver_profiles/', blank=True, null=True)
    driver_license = models.ImageField(upload_to='driver_license/', blank=True, null=True)

    VEHICLE_CHOICES = [
        ('Tricycle', 'Tricycle'),
        ('Motorcycle', 'Motorcycle'),
        ('Multicab', 'Multicab'),
        ('Bus', 'Bus')
    ]
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_CHOICES)
    availability = models.CharField(max_length=100)  # e.g. 8AM - 5PM
    travel_area = models.CharField(max_length=100)   # e.g. San Juan, Taft

    def __str__(self):
        return f"{self.user.username} - {self.vehicle_type}"
