from django.conf import settings
from django.core.checks import CheckMessage, Error, register

REQUIRED_KEYS = [
    "rdf_root",
]


@register("settings")
def check_residential_settings(
    app_configs: None = None,  # noqa: ARG001
    **_: dict[str, object],
) -> list[CheckMessage]:
    errors = []
    if not hasattr(settings, "RESIDENTIAL"):
        errors.append(
            Error(
                "Missing RESIDENTIAL settings",
                hint="RESIDENTIAL settings must be provided",
                id="illallangi.data.residential.E005",
            )
        )
    elif not isinstance(settings.RESIDENTIAL, dict):
        errors.append(
            Error(
                "Invalid RESIDENTIAL settings",
                hint="RESIDENTIAL settings must be a dictionary",
                id="illallangi.data.residential.E006",
            )
        )
    else:
        if len(settings.RESIDENTIAL) != len(REQUIRED_KEYS):
            errors.append(
                Error(
                    "Invalid RESIDENTIAL settings",
                    hint=f"RESIDENTIAL settings must contain exactly {len(REQUIRED_KEYS)} keys",
                    id="illallangi.data.residential.E007",
                )
            )
        [
            errors.append(
                Error(
                    f"Missing RESIDENTIAL setting {key}",
                    hint=f"RESIDENTIAL setting {key} must be provided",
                    id="illallangi.data.residential.E008",
                ),
            )
            for key in REQUIRED_KEYS
            if key not in settings.RESIDENTIAL or not settings.RESIDENTIAL[key]
        ]
    return errors
