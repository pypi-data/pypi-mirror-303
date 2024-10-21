from django.apps import AppConfig
from django.conf import settings

from illallangi.django.home.models.models_manager import ModelsManager
from illallangi.tripit.adapters import AirTransportAdapter as TripItAdapter


class AirTransportConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "illallangi.data.air_transport"

    def ready(self) -> None:
        ModelsManager().add_model(
            singular="Flight",
            plural="Flights",
            model="illallangi.data.air_transport.models.Flight",
            url="flights_html",
            icon="air_transport/flights.jpg",
            description="Every leg of a journey, no matter how long or short, brings you closer to your destination.",
        )
        ModelsManager().add_model(
            singular="Trip",
            plural="Trips",
            model="illallangi.data.air_transport.models.Trip",
            url="trips_html",
            icon="air_transport/trips.jpg",
            description="Each trip is a step towards discovering new horizons, embracing diverse cultures, and enriching your soul.",
        )

        def synchronize() -> None:
            from illallangi.data.air_transport.adapters import (
                AirTransportAdapter as DjangoAdapter,
            )

            src = TripItAdapter(
                **settings.TRIPIT,
            )
            dst = DjangoAdapter()

            src.load(
                **settings.AIR_TRANSPORT,
            )
            dst.load()

            src.sync_to(dst)

        ModelsManager().add_synchronize(
            name=__name__,
            synchronize=synchronize,
        )
