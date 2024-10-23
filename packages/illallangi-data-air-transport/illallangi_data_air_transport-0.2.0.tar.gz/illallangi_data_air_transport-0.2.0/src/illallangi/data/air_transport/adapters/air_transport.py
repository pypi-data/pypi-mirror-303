from typing import ClassVar

import diffsync

from illallangi.data.air_transport.diffsyncmodels import Flight, Trip
from illallangi.data.air_transport.models import Flight as DjangoFlight
from illallangi.data.air_transport.models import Trip as DjangoTrip


class AirTransportAdapter(diffsync.Adapter):
    Flight = Flight
    Trip = Trip

    top_level: ClassVar = [
        "Flight",
        "Trip",
    ]

    type = "django_air_transport"

    def load(
        self,
    ) -> None:
        for obj in DjangoFlight.objects.all():
            self.add(
                Flight(
                    pk=obj.pk,
                    departure=obj.departure,
                    flight_number=obj.flight_number,
                    airline=obj.airline.iata,
                    arrival_timezone=str(obj.arrival_timezone),
                    arrival=obj.arrival,
                    departure_timezone=str(obj.departure_timezone),
                    destination_city=obj.destination_city,
                    destination_gate=obj.destination_gate,
                    destination_terminal=obj.destination_terminal,
                    destination=obj.destination.iata,
                    flight_class=obj.flight_class,
                    origin_city=obj.origin_city,
                    origin_gate=obj.origin_gate,
                    origin_terminal=obj.origin_terminal,
                    origin=obj.origin.iata,
                    passenger=obj.passenger,
                    seat=obj.seat,
                    sequence_number=obj.sequence_number,
                ),
            )
        for obj in DjangoTrip.objects.all():
            self.add(
                Trip(
                    pk=obj.pk,
                    name=obj.name,
                    start=obj.start,
                    end=obj.end,
                ),
            )
