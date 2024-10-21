from django.conf import settings
from django.core.checks import CheckMessage, Error, register

REQUIRED_KEYS = [
    "tripit_access_token_secret",
    "tripit_access_token",
    "tripit_client_token_secret",
    "tripit_client_token",
]


@register("settings")
def check_tripit_settings(
    app_configs: None = None,  # noqa: ARG001
    **_: dict[str, object],
) -> list[CheckMessage]:
    errors = []
    if not hasattr(settings, "TRIPIT"):
        errors.append(
            Error(
                "Missing TRIPIT settings",
                hint="TRIPIT settings must be provided",
                id="illallangi.data.air_transport.E001",
            )
        )
    elif not isinstance(settings.TRIPIT, dict):
        errors.append(
            Error(
                "Invalid TRIPIT settings",
                hint="TRIPIT settings must be a dictionary",
                id="illallangi.data.air_transport.E002",
            )
        )
    else:
        if len(settings.TRIPIT) != len(REQUIRED_KEYS):
            errors.append(
                Error(
                    "Invalid TRIPIT settings",
                    hint=f"TRIPIT settings must contain exactly {len(REQUIRED_KEYS)} keys",
                    id="illallangi.data.air_transport.E003",
                )
            )
        [
            errors.append(
                Error(
                    f"Missing TRIPIT setting {key}",
                    hint=f"TRIPIT setting {key} must be provided",
                    id="illallangi.data.air_transport.E004",
                ),
            )
            for key in REQUIRED_KEYS
            if key not in settings.TRIPIT or not settings.TRIPIT[key]
        ]
    return errors
