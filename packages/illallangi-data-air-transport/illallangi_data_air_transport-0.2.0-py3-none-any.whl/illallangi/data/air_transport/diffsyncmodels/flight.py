from datetime import datetime

import diffsync

from illallangi.data.air_transport.models import Flight as ModelFlight
from illallangi.data.aviation.models import Airline, Airport


class Flight(
    diffsync.DiffSyncModel,
):
    _modelname = "Flight"
    _identifiers = (
        "departure",
        "flight_number",
    )
    _attributes = (
        "airline",
        "arrival",
        "arrival_timezone",
        "departure_timezone",
        "destination",
        "destination_city",
        "destination_terminal",
        "flight_class",
        "origin",
        "origin_city",
        "origin_terminal",
        "sequence_number",
        "seat",
        "passenger",
    )

    pk: int

    departure: datetime
    flight_number: str

    airline: str
    arrival_timezone: str
    arrival: datetime
    departure_timezone: str
    destination_city: str
    destination_gate: str
    destination_terminal: str
    destination: str
    flight_class: str
    origin_city: str
    origin_gate: str
    origin_terminal: str
    origin: str
    passenger: str
    seat: str
    sequence_number: str

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Flight":
        destination_airport = Airport.objects.get_or_create(iata=attrs["destination"])[
            0
        ]
        origin_airport = Airport.objects.get_or_create(iata=attrs["origin"])[0]

        airline = Airline.objects.get_or_create(iata=attrs["airline"])[0]

        obj = ModelFlight.objects.update_or_create(
            departure=ids["departure"],
            flight_number=ids["flight_number"],
            defaults={
                "airline": airline,
                "arrival_timezone": attrs["arrival_timezone"],
                "arrival": attrs["arrival"],
                "departure_timezone": attrs["departure_timezone"],
                "destination_city": attrs["destination_city"],
                "destination_gate": attrs["destination_gate"],
                "destination_terminal": attrs["destination_terminal"],
                "destination": destination_airport,
                "flight_class": attrs["flight_class"],
                "origin_city": attrs["origin_city"],
                "origin_gate": attrs["origin_gate"],
                "origin_terminal": attrs["origin_terminal"],
                "origin": origin_airport,
                "passenger": attrs["passenger"],
                "seat": attrs["seat"],
                "sequence_number": attrs["sequence_number"],
            },
        )[0]

        return super().create(
            adapter,
            {
                "pk": obj.pk,
                **ids,
            },
            attrs,
        )

    def update(
        self,
        attrs: dict,
    ) -> "Flight":
        destination_airport = Airport.objects.get_or_create(iata=attrs["destination"])[
            0
        ]
        origin_airport = Airport.objects.get_or_create(iata=attrs["origin"])[0]

        airline = Airline.objects.get_or_create(iata=attrs["airline"])[0]

        ModelFlight.objects.filter(
            pk=self.pk,
        ).update(
            **{
                **attrs,
                "airline": airline,
                "destination": destination_airport,
                "origin": origin_airport,
            },
        )

        return super().update(attrs)

    def delete(
        self,
    ) -> "Flight":
        ModelFlight.objects.get(
            pk=self.pk,
        ).delete()

        return super().delete()
