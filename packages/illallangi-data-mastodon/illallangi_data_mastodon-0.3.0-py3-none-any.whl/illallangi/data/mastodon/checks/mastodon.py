from django.conf import settings
from django.core.checks import CheckMessage, Error, register

REQUIRED_KEYS = [
    "mastodon_user",
]


@register("settings")
def check_mastodon_settings(
    app_configs: None = None,  # noqa: ARG001
    **_: dict[str, object],
) -> list[CheckMessage]:
    errors = []
    if not hasattr(settings, "MASTODON"):
        errors.append(
            Error(
                "Missing MASTODON settings",
                hint="MASTODON settings must be provided",
                id="illallangi.data.mastodon.E001",
            )
        )
    elif not isinstance(settings.MASTODON, dict):
        errors.append(
            Error(
                "Invalid MASTODON settings",
                hint="MASTODON settings must be a dictionary",
                id="illallangi.data.mastodon.E002",
            )
        )
    else:
        if len(settings.MASTODON) != len(REQUIRED_KEYS):
            errors.append(
                Error(
                    "Invalid MASTODON settings",
                    hint=f"MASTODON settings must contain exactly {len(REQUIRED_KEYS)} keys",
                    id="illallangi.data.mastodon.E003",
                )
            )
        [
            errors.append(
                Error(
                    f"Missing MASTODON setting {key}",
                    hint=f"MASTODON setting {key} must be provided",
                    id="illallangi.data.mastodon.E004",
                ),
            )
            for key in REQUIRED_KEYS
            if key not in settings.MASTODON or not settings.MASTODON[key]
        ]
    return errors
