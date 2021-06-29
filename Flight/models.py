from django.db import models

class AirportModel(models.Model):
    code = models.CharField(max_length=64)
    city = models.CharField(max_length=64)


    def __str__(self):
        return f"{self.city} ({self.code})"

    class Meta:
        verbose_name = 'airport'
        verbose_name_plural = 'airports'



class FlightModel(models.Model):
    origin = models.ForeignKey(AirportModel, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(AirportModel, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()


    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}"

    class Meta:
        verbose_name = 'flight'
        verbose_name_plural = 'flights'

class PassengerModel(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    flights = models.ManyToManyField(FlightModel, blank=True, related_name='passenger')

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

    class Meta:
        verbose_name = 'passenger'
        verbose_name_plural = 'passengers'

