from django.conf import settings
from django.core.checks import CheckMessage, Error, register

REQUIRED_KEYS = []


@register("settings")
def check_air_transport_settings(
    app_configs: None = None,  # noqa: ARG001
    **_: dict[str, object],
) -> list[CheckMessage]:
    errors = []
    if not hasattr(settings, "AIR_TRANSPORT"):
        errors.append(
            Error(
                "Missing AIR_TRANSPORT settings",
                hint="AIR_TRANSPORT settings must be provided",
                id="illallangi.data.air_transport.E005",
            )
        )
    elif not isinstance(settings.AIR_TRANSPORT, dict):
        errors.append(
            Error(
                "Invalid AIR_TRANSPORT settings",
                hint="AIR_TRANSPORT settings must be a dictionary",
                id="illallangi.data.air_transport.E006",
            )
        )
    else:
        if len(settings.AIR_TRANSPORT) != len(REQUIRED_KEYS):
            errors.append(
                Error(
                    "Invalid AIR_TRANSPORT settings",
                    hint=f"AIR_TRANSPORT settings must contain exactly {len(REQUIRED_KEYS)} keys",
                    id="illallangi.data.air_transport.E007",
                )
            )
        [
            errors.append(
                Error(
                    f"Missing AIR_TRANSPORT setting {key}",
                    hint=f"AIR_TRANSPORT setting {key} must be provided",
                    id="illallangi.data.air_transport.E008",
                ),
            )
            for key in REQUIRED_KEYS
            if key not in settings.AIR_TRANSPORT or not settings.AIR_TRANSPORT[key]
        ]
    return errors
