from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Sample data structure for seats (could later be replaced by database)
seats = {
    'A1': None,'A2': None,  # None means the seat is available
    'A3': None,'A4': None,'A5': None,'A6': None,'A7': None,'A8': None,'A9': None,
    'A10': None,'A11': None,'A12': None,'A13': None,'A14': None,'A15': None,'A16': None,
    'A17': None,'A18': None,'A19': None,'A20': None,
}

def home(request):
    return render(request, 'index.html')

# Booking View
def booking(request):
    if request.method == "POST":
        seat_number = request.POST.get('seat')
        passenger_name = request.POST.get('name')
        if seat_number in seats and seats[seat_number] is None:
            seats[seat_number] = passenger_name  # Book the seat
            messages.success(request, f"Seat {seat_number} booked successfully for {passenger_name}!")
        else:
            messages.error(request, f"Seat {seat_number} is already booked or invalid!")
        return redirect('booking')
    
    available_seats = [seat for seat, passenger in seats.items() if passenger is None]
    context = {
        'available_seats': available_seats
    }
    return render(request, 'booking.html', context)

# Cancel Booking View
def cancel(request):
    if request.method == "POST":
        seat_number = request.POST.get('seat')
        if seat_number in seats and seats[seat_number] is not None:
            seats[seat_number] = None  # Cancel the seat
            messages.success(request, f"Seat {seat_number} canceled successfully!")
        else:
            messages.error(request, f"Seat {seat_number} is not booked or invalid!")
        return redirect('cancel')
    
    booked_seats = [seat for seat, passenger in seats.items() if passenger is not None]
    context = {
        'booked_seats': booked_seats
    }
    return render(request, 'cancel.html', context)

# Check Availability View
def availability(request):
    available_seats = [seat for seat, passenger in seats.items() if passenger is None]
    context = {
        'available_seats': available_seats
    }
    return render(request, 'availability.html', context)


'''
def home(request):
    return render(request, 'index.html')

def booking(request):
    # Logic for booking
    return render(request, 'booking.html')

def cancel(request):
    # Logic for cancelling booking
    return render(request, 'cancel.html')

def availability(request):
    # Logic for checking availability
    return render(request, 'availability.html')
'''

