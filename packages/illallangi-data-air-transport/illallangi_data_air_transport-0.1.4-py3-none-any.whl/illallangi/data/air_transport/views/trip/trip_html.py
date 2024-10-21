import calendar

from django.contrib.humanize.templatetags.humanize import ordinal
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.data.air_transport.models import Trip


@require_GET
def trip_html(
    request: HttpRequest,
    trip_year: str,
    trip_month: str,
    trip_day: str,
    trip_slug: str,
) -> render:
    objects = Trip.objects.filter(
        start__year=trip_year,
        start__month=trip_month,
        start__day=trip_day,
        slug=trip_slug,
    )

    if objects.count() > 1:
        return HttpResponse(
            status=500,
            content="Multiple trips found for slug",
        )

    if objects.count() == 1:
        obj = objects.first()
        return render(
            request,
            "air_transport/trip.html",
            {
                "base_template": ("partial.html" if request.htmx else "base.html"),
                "obj": obj,
                "breadcrumbs": [
                    {
                        "title": "Trips",
                        "url": reverse(
                            "trips_html",
                        ),
                    },
                    {
                        "title": obj.start.year,
                        "url": reverse(
                            "trips_year",
                            kwargs={
                                "trip_year": str(obj.start.year).zfill(4),
                            },
                        ),
                    },
                    {
                        "title": calendar.month_name[obj.start.month],
                        "url": reverse(
                            "trips_month",
                            kwargs={
                                "trip_year": str(obj.start.year).zfill(4),
                                "trip_month": str(obj.start.month).zfill(2),
                            },
                        ),
                    },
                    {
                        "title": ordinal(obj.start.day),
                        "url": reverse(
                            "trips_day",
                            kwargs={
                                "trip_year": str(obj.start.year).zfill(4),
                                "trip_month": str(obj.start.month).zfill(2),
                                "trip_day": str(obj.start.day).zfill(2),
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
                ],
            },
        )

    return HttpResponse(
        status=400,
        content="Trip not found",
    )
