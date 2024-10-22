from django.conf import settings
from django.core.checks import CheckMessage, Error, register

REQUIRED_KEYS = []


@register("settings")
def check_fitness_settings(
    app_configs: None = None,  # noqa: ARG001
    **_: dict[str, object],
) -> list[CheckMessage]:
    errors = []
    if not hasattr(settings, "FITNESS"):
        errors.append(
            Error(
                "Missing FITNESS settings",
                hint="FITNESS settings must be provided",
                id="illallangi.data.fitness.E005",
            )
        )
    elif not isinstance(settings.FITNESS, dict):
        errors.append(
            Error(
                "Invalid FITNESS settings",
                hint="FITNESS settings must be a dictionary",
                id="illallangi.data.fitness.E006",
            )
        )
    else:
        if len(settings.FITNESS) != len(REQUIRED_KEYS):
            errors.append(
                Error(
                    "Invalid FITNESS settings",
                    hint=f"FITNESS settings must contain exactly {len(REQUIRED_KEYS)} keys",
                    id="illallangi.data.fitness.E007",
                )
            )
        [
            errors.append(
                Error(
                    f"Missing FITNESS setting {key}",
                    hint=f"FITNESS setting {key} must be provided",
                    id="illallangi.data.fitness.E008",
                ),
            )
            for key in REQUIRED_KEYS
            if key not in settings.FITNESS or not settings.FITNESS[key]
        ]
    return errors
