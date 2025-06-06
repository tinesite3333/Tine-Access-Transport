from django import forms
from .models import DriverProfile

class DriverProfileForm(forms.ModelForm):
    class Meta:
        model = DriverProfile
        fields = ['contact_number', 'vehicle_type', 'availability', 'travel_area', 'profile_picture', 'driver_license'] 

        widgets = {
            'availability': forms.TextInput(attrs={'placeholder': 'e.g. 8AM - 5PM'}),
            'travel_area': forms.TextInput(attrs={'placeholder': 'e.g. San Juan, Taft'}),
        }
