from datetime import datetime, timedelta

from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django_sqids import SqidsField
from timezone_field import TimeZoneField

from illallangi.data.aviation.models import Airline, Airport


class Flight(
    models.Model,
):
    # Surrogate Keys

    id = models.AutoField(
        primary_key=True,
    )

    slug = AutoSlugField(
        populate_from="get_slug",
        unique_with=(
            "departure__year",
            "departure__month",
            "departure__day",
        ),
    )

    sqid = SqidsField(
        real_field_name="id",
        min_length=6,
    )

    # Natural Keys

    departure = models.DateTimeField(
        null=False,
    )

    flight_number = models.CharField(
        null=False,
        max_length=6,
    )

    # Fields

    airline = models.ForeignKey(
        to=Airline,
        on_delete=models.CASCADE,
        related_name="flights",
    )

    arrival = models.DateTimeField(
        null=False,
        max_length=25,
    )

    arrival_timezone = TimeZoneField(
        null=False,
    )

    departure_timezone = TimeZoneField(
        null=False,
    )

    destination = models.ForeignKey(
        to=Airport,
        on_delete=models.CASCADE,
        related_name="destination_flights",
    )

    destination_city = models.CharField(
        null=False,
        max_length=255,
    )

    passenger = models.CharField(
        null=False,
        max_length=255,
    )

    destination_terminal = models.CharField(
        null=False,
        max_length=255,
    )

    destination_gate = models.CharField(
        null=False,
        max_length=255,
    )

    flight_class = models.CharField(
        null=False,
        max_length=255,
    )

    origin = models.ForeignKey(
        to=Airport,
        on_delete=models.CASCADE,
        related_name="originating_flights",
    )

    origin_city = models.CharField(
        null=False,
        max_length=255,
    )

    origin_gate = models.CharField(
        null=False,
        max_length=255,
    )

    origin_terminal = models.CharField(
        null=False,
        max_length=255,
    )

    sequence_number = models.CharField(
        null=False,
        max_length=3,
    )

    seat = models.CharField(
        null=False,
        max_length=3,
    )

    # Classes

    class Meta:
        unique_together = ("departure", "slug")

    # Methods

    def __str__(
        self,
    ) -> str:
        return self.flight_number

    def get_absolute_url(
        self,
    ) -> str:
        return reverse(
            "flight_html",
            kwargs={
                "flight_slug": str(self.slug),
                "flight_year": str(self.departure.year).zfill(4),
                "flight_month": str(self.departure.month).zfill(2),
                "flight_day": str(self.departure.day).zfill(2),
            },
        )

    @property
    def description(
        self,
    ) -> str:
        return f"A {self.airline.label or self.airline} flight from {self.origin_city} to {self.destination_city}"

    @property
    def boarding(
        self,
    ) -> datetime:
        return self.departure - timedelta(minutes=30)

    @property
    def boarding_timezone(
        self,
    ) -> str:
        return self.departure_timezone

    @property
    def boarding_date_local(
        self,
    ) -> str:
        return self.boarding.astimezone(self.boarding_timezone).strftime("%d%b")

    @property
    def boarding_time_local(
        self,
    ) -> str:
        return self.boarding.astimezone(self.boarding_timezone).strftime("%H%M")

    @property
    def departure_date_local(
        self,
    ) -> str:
        return self.departure.astimezone(self.departure_timezone).strftime("%d%b")

    @property
    def departure_time_local(
        self,
    ) -> str:
        return self.departure.astimezone(self.departure_timezone).strftime("%H%M")

    @property
    def arrival_date_local(
        self,
    ) -> str:
        return self.arrival.astimezone(self.arrival_timezone).strftime("%d%b")

    @property
    def arrival_time_local(
        self,
    ) -> str:
        return self.arrival.astimezone(self.arrival_timezone).strftime("%H%M")

    def get_slug(
        self,
    ) -> str:
        return self.flight_number.replace(" ", "")
