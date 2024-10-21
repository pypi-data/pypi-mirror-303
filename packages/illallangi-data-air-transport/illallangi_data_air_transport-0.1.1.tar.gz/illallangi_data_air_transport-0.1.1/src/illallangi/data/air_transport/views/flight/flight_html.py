import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.air_transport.models import Flight


@require_GET
def flight_html(
    request: HttpRequest,
    flight_year: str,
    flight_month: str,
    flight_day: str,
    flight_slug: str,
) -> render:
    objects = Flight.objects.filter(
        departure__year=flight_year,
        departure__month=flight_month,
        departure__day=flight_day,
        slug=flight_slug,
    )

    if objects.count() > 1:
        return HttpResponse(
            status=500,
            content="Multiple flights found for slug",
        )

    if objects.count() == 1:
        obj = objects.first()
        return render(
            request,
            "air_transport/flight.html",
            {
                "base_template": ("partial.html" if request.htmx else "base.html"),
                "obj": obj,
                "breadcrumbs": [
                    {
                        "title": "Flights",
                        "url": reverse(
                            "flights_html",
                        ),
                    },
                    {
                        "title": obj.departure.year,
                        "url": reverse(
                            "flights_year",
                            kwargs={
                                "flight_year": str(obj.departure.year).zfill(4),
                            },
                        ),
                    },
                    {
                        "title": calendar.month_name[obj.departure.month],
                        "url": reverse(
                            "flights_month",
                            kwargs={
                                "flight_year": str(obj.departure.year).zfill(4),
                                "flight_month": str(obj.departure.month).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": ordinal(obj.departure.day),
                        "url": reverse(
                            "flights_day",
                            kwargs={
                                "flight_year": str(obj.departure.year).zfill(4),
                                "flight_month": str(obj.departure.month).zfill(2),
                                "flight_day": str(obj.departure.day).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": str(obj),
                        "url": obj.get_absolute_url(),
                    },
                ],
                "links": [
                    {
                        "rel": "alternate",
                        "type": "text/html",
                        "href": request.build_absolute_uri(
                            obj.get_absolute_url(),
                        ),
                    },
                    {
                        "rel": "stylesheet",
                        "href": static("air_transport/flight.css"),
                    },
                ],
            },
        )

    return HttpResponse(
        status=400,
        content="Flight not found",
    )
