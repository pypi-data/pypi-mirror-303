import djp
from django.urls import URLPattern, re_path

from illallangi.data.air_transport import checks  # noqa: F401


@djp.hookimpl
def installed_apps() -> list[str]:
    return [
        "illallangi.data.air_transport",
    ]


@djp.hookimpl
def urlpatterns() -> list[URLPattern]:
    from illallangi.data.air_transport import views

    return [
        re_path(
            r"^trips/$",
            views.trips_html,
            name="trips_html",
        ),
        re_path(
            r"^trips/(?P<trip_year>[0-9]{4})/$",
            views.trips_html,
            name="trips_year",
        ),
        re_path(
            r"^trips/(?P<trip_year>[0-9]{4})/(?P<trip_month>[0-9]{2})/$",
            views.trips_html,
            name="trips_month",
        ),
        re_path(
            r"^trips/(?P<trip_year>[0-9]{4})/(?P<trip_month>[0-9]{2})/(?P<trip_day>[0-9]{2})/$",
            views.trips_html,
            name="trips_day",
        ),
        re_path(
            r"^trips/(?P<trip_year>[0-9]{4})/(?P<trip_month>[0-9]{2})/(?P<trip_day>[0-9]{2})/(?P<trip_slug>[\w\d-]+)/$",
            views.trip_html,
            name="trip_html",
        ),
        re_path(
            r"^flights/$",
            views.flights_html,
            name="flights_html",
        ),
        re_path(
            r"^flights/(?P<flight_year>[0-9]{4})/$",
            views.flights_html,
            name="flights_year",
        ),
        re_path(
            r"^flights/(?P<flight_year>[0-9]{4})/(?P<flight_month>[0-9]{2})/$",
            views.flights_html,
            name="flights_month",
        ),
        re_path(
            r"^flights/(?P<flight_year>[0-9]{4})/(?P<flight_month>[0-9]{2})/(?P<flight_day>[0-9]{2})/$",
            views.flights_html,
            name="flights_day",
        ),
        re_path(
            r"^flights/(?P<flight_year>[0-9]{4})/(?P<flight_month>[0-9]{2})/(?P<flight_day>[0-9]{2})/(?P<flight_slug>[\w\d-]+)/$",
            views.flight_html,
            name="flight_html",
        ),
    ]
