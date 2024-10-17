from django import forms
from .models import BusBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = BusBooking
        fields = ['passenger_name', 'bus_number', 'seat_number']

class CancelForm(forms.Form):
    bus_number = forms.CharField(max_length=20)
    seat_number = forms.IntegerField()
