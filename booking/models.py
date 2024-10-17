from django.db import models

# Create your models here.

class BusBooking(models.Model):
    passenger_name = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=20)
    seat_number = models.IntegerField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.passenger_name} - Bus {self.bus_number} - Seat {self.seat_number}'
