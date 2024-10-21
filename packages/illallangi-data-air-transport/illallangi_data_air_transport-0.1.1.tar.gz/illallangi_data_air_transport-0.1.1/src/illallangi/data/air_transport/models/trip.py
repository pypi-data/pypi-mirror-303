from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django_sqids import SqidsField


class Trip(
    models.Model,
):
    # Surrogate Keys

    id = models.AutoField(
        primary_key=True,
    )

    slug = AutoSlugField(
        populate_from="get_slug",
        unique_with=(
            "start__year",
            "start__month",
            "start__day",
        ),
    )

    sqid = SqidsField(
        real_field_name="id",
        min_length=6,
    )

    # Natural Keys

    start = models.DateField(
        null=False,
    )

    name = models.CharField(
        null=False,
        max_length=64,
    )

    # Fields

    end = models.DateField(
        null=False,
        max_length=25,
    )

    # Classes

    class Meta:
        unique_together = ("start", "slug")

    # Methods

    def __str__(
        self,
    ) -> str:
        return self.name

    def get_absolute_url(
        self,
    ) -> str:
        return reverse(
            "trip_html",
            kwargs={
                "trip_slug": str(self.slug),
                "trip_year": str(self.start.year).zfill(4),
                "trip_month": str(self.start.month).zfill(2),
                "trip_day": str(self.start.day).zfill(2),
            },
        )

    @property
    def description(
        self,
    ) -> str:
        return f"A {self.end - self.start} trip"

    def get_slug(
        self,
    ) -> str:
        return self.name
