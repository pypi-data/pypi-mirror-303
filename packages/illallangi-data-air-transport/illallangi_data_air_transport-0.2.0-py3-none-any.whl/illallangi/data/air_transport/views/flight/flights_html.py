import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.templatetags.static import static
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.air_transport.models import Flight


@require_GET
def flights_html(
    request: HttpRequest,
    flight_year: str | None = None,
    flight_month: str | None = None,
    flight_day: str | None = None,
    **_: dict,
) -> render:
    objects = Flight.objects.all()
    if flight_year:
        objects = objects.filter(departure__year=flight_year)
    if flight_month:
        objects = objects.filter(departure__month=flight_month)
    if flight_day:
        objects = objects.filter(departure__day=flight_day)

    if objects.count() == 1:
        return redirect(
            objects.first().get_absolute_url(),
        )

    return render(
        request,
        "air_transport/flights.html",
        {
            "base_template": ("partial.html" if request.htmx else "base.html"),
            "page": Paginator(
                object_list=objects.order_by("departure"),
                per_page=10,
            ).get_page(
                request.GET.get("page", 1),
            ),
            "breadcrumbs": list(
                filter(
                    lambda x: x is not None,
                    [
                        {
                            "title": "Flights",
                            "url": reverse(
                                "flights_html",
                            ),
                        },
                        {
                            "title": flight_year,
                            "url": reverse(
                                "flights_year",
                                kwargs={
                                    "flight_year": flight_year,
                                },
                            ),
                        }
                        if flight_year
                        else None,
                        {
                            "title": calendar.month_name[int(flight_month)],
                            "url": reverse(
                                "flights_month",
                                kwargs={
                                    "flight_year": flight_year,
                                    "flight_month": flight_month,
                                },
                            ),
                        }
                        if flight_month
                        else None,
                        {
                            "title": ordinal(flight_day),
                            "url": reverse(
                                "flights_day",
                                kwargs={
                                    "flight_year": flight_year,
                                    "flight_month": flight_month,
                                    "flight_day": flight_day,
                                },
                            ),
                        }
                        if flight_day
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
                            "flights_html",
                        ),
                    ),
                },
                {
                    "rel": "stylesheet",
                    "href": static("air_transport/flight.css"),
                },
            ],
        },
    )
