from django.contrib import admin

from Flight.models import FlightModel, AirportModel, PassengerModel


@admin.register(FlightModel)
class FlightModelAdmin(admin.ModelAdmin):
    list_display = ['origin', 'destination', 'duration']
    list_filter = ['duration']
    search_fields = ['origin', 'destination']

@admin.register(AirportModel)
class AirportModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'city']
    list_filter = ['code']
    search_fields = ['code', 'city']

@admin.register(PassengerModel)
class PassengerModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['last_name']
    search_fields = ['first_name', 'last_name']

