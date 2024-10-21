from django.conf import settings
from django.core.checks import CheckMessage, Error, register

REQUIRED_KEYS = [
    "rdf_root",
]


@register("settings")
def check_education_settings(
    app_configs: None = None,  # noqa: ARG001
    **_: dict[str, object],
) -> list[CheckMessage]:
    errors = []
    if not hasattr(settings, "EDUCATION"):
        errors.append(
            Error(
                "Missing EDUCATION settings",
                hint="EDUCATION settings must be provided",
                id="illallangi.data.education.E005",
            )
        )
    elif not isinstance(settings.EDUCATION, dict):
        errors.append(
            Error(
                "Invalid EDUCATION settings",
                hint="EDUCATION settings must be a dictionary",
                id="illallangi.data.education.E006",
            )
        )
    else:
        if len(settings.EDUCATION) != len(REQUIRED_KEYS):
            errors.append(
                Error(
                    "Invalid EDUCATION settings",
                    hint=f"EDUCATION settings must contain exactly {len(REQUIRED_KEYS)} keys",
                    id="illallangi.data.education.E007",
                )
            )
        [
            errors.append(
                Error(
                    f"Missing EDUCATION setting {key}",
                    hint=f"EDUCATION setting {key} must be provided",
                    id="illallangi.data.education.E008",
                ),
            )
            for key in REQUIRED_KEYS
            if key not in settings.EDUCATION or not settings.EDUCATION[key]
        ]
    return errors
