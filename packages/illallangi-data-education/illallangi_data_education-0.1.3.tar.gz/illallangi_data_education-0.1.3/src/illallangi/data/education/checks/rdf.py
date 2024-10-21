from django.conf import settings
from django.core.checks import CheckMessage, Error, register

REQUIRED_KEYS = [
    "github_file_path",
    "github_repo_name",
    "github_repo_owner",
    "github_token",
]


@register("settings")
def check_rdf_settings(
    app_configs: None = None,  # noqa: ARG001
    **_: dict[str, object],
) -> list[CheckMessage]:
    errors = []
    if not hasattr(settings, "RDF"):
        errors.append(
            Error(
                "Missing RDF settings",
                hint="RDF settings must be provided",
                id="illallangi.data.education.E001",
            )
        )
    elif not isinstance(settings.RDF, dict):
        errors.append(
            Error(
                "Invalid RDF settings",
                hint="RDF settings must be a dictionary",
                id="illallangi.data.education.E002",
            )
        )
    else:
        if len(settings.RDF) != len(REQUIRED_KEYS):
            errors.append(
                Error(
                    "Invalid RDF settings",
                    hint=f"RDF settings must contain exactly {len(REQUIRED_KEYS)} keys",
                    id="illallangi.data.education.E003",
                )
            )
        [
            errors.append(
                Error(
                    f"Missing RDF setting {key}",
                    hint=f"RDF setting {key} must be provided",
                    id="illallangi.data.education.E004",
                ),
            )
            for key in REQUIRED_KEYS
            if key not in settings.RDF or not settings.RDF[key]
        ]
    return errors
