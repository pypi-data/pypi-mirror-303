import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.air_transport.models import Trip


@require_GET
def trips_html(
    request: HttpRequest,
    trip_year: str | None = None,
    trip_month: str | None = None,
    trip_day: str | None = None,
    **_: dict,
) -> render:
    objects = Trip.objects.all()
    if trip_year:
        objects = objects.filter(start__year=trip_year)
    if trip_month:
        objects = objects.filter(start__month=trip_month)
    if trip_day:
        objects = objects.filter(start__day=trip_day)

    if objects.count() == 1:
        return redirect(
            objects.first().get_absolute_url(),
        )

    return render(
        request,
        "air_transport/trips.html",
        {
            "base_template": ("partial.html" if request.htmx else "base.html"),
            "page": Paginator(
                object_list=objects.order_by("start"),
                per_page=10,
            ).get_page(
                request.GET.get("page", 1),
            ),
            "breadcrumbs": list(
                filter(
                    lambda x: x is not None,
                    [
                        {
                            "title": "Trips",
                            "url": reverse(
                                "trips_html",
                            ),
                        },
                        {
                            "title": trip_year,
                            "url": reverse(
                                "trips_year",
                                kwargs={
                                    "trip_year": trip_year,
                                },
                            ),
                        }
                        if trip_year
                        else None,
                        {
                            "title": calendar.month_name[int(trip_month)],
                            "url": reverse(
                                "trips_month",
                                kwargs={
                                    "trip_year": trip_year,
                                    "trip_month": trip_month,
                                },
                            ),
                        }
                        if trip_month
                        else None,
                        {
                            "title": ordinal(trip_day),
                            "url": reverse(
                                "trips_day",
                                kwargs={
                                    "trip_year": trip_year,
                                    "trip_month": trip_month,
                                    "trip_day": trip_day,
                                },
                            ),
                        }
                        if trip_day
                        else None,
                    ],
                )
            ),
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "href": request.build_absolute_uri(
                        reverse(
                            "trips_html",
                        ),
                    ),
                },
            ],
        },
    )
