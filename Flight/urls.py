from django.urls import path

from Flight.views import index, flight, book

urlpatterns = [
    path('flight/', index, name='index'),
    path("<int:flight_id>", flight, name='flight'),
    path("<int:flight_id>/book/", book, name= 'book')
]