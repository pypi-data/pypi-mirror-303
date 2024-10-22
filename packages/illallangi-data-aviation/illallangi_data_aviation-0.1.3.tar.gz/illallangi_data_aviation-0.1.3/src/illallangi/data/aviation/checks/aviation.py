from django.conf import settings
from django.core.checks import CheckMessage, Error, register

REQUIRED_KEYS = []


@register("settings")
def check_aviation_settings(
    app_configs: None = None,  # noqa: ARG001
    **_: dict[str, object],
) -> list[CheckMessage]:
    errors = []
    if not hasattr(settings, "AVIATION"):
        errors.append(
            Error(
                "Missing AVIATION settings",
                hint="AVIATION settings must be provided",
                id="illallangi.data.aviation.E005",
            )
        )
    elif not isinstance(settings.AVIATION, dict):
        errors.append(
            Error(
                "Invalid AVIATION settings",
                hint="AVIATION settings must be a dictionary",
                id="illallangi.data.aviation.E006",
            )
        )
    else:
        if len(settings.AVIATION) != len(REQUIRED_KEYS):
            errors.append(
                Error(
                    "Invalid AVIATION settings",
                    hint=f"AVIATION settings must contain exactly {len(REQUIRED_KEYS)} keys",
                    id="illallangi.data.aviation.E007",
                )
            )
        [
            errors.append(
                Error(
                    f"Missing AVIATION setting {key}",
                    hint=f"AVIATION setting {key} must be provided",
                    id="illallangi.data.aviation.E008",
                ),
            )
            for key in REQUIRED_KEYS
            if key not in settings.AVIATION or not settings.AVIATION[key]
        ]
    return errors
