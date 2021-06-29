from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from Flight.models import FlightModel, PassengerModel


def index(request):
    context = {
        "flights": FlightModel.objects.all()
    }
    return render(request, 'index.html', context)


def flight(request, flight_id):
    try:
        flights = FlightModel.objects.get(pk=flight_id)
    except FlightModel.DoesNotExist:
        raise Http404("Flight does not exist.",)
    context ={
        "flights": flights,
        "passengers": flights.passenger.all(),
        "non_passengers":PassengerModel.objects.exclude(flights=flight_id)
    }
    return render(request, 'flight.html',context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST['passenger'])
        passenger = PassengerModel.objects.get(pk=passenger_id)
        flight = FlightModel.objects.get(pk=flight_id)
    except FlightModel.DoesNotExist:
        return render(request, 'error.html', {"message": "No flight"})
    except PassengerModel.DoesNotExist:
        return render(request, 'error.html', {"messageme": "No passenger"})

    passenger.flights.add(flight)
    return redirect(reverse("flight", args=(flight_id, )))




