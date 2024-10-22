from django.apps import AppConfig
from django.conf import settings

from illallangi.django.data.models.models_manager import ModelsManager
from illallangi.mastodon.adapters import MastodonAdapter


class MastodonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "illallangi.data.mastodon"

    def ready(self) -> None:
        ModelsManager().add_model(
            singular="Status",
            plural="Statuses",
            model="illallangi.data.mastodon.models.Status",
            url="statuses_html",
            icon="mastodon/statuses.png",
            description="Each status is a step towards discovering new horizons, embracing diverse cultures, and enriching your soul.",
        )

        def synchronize() -> None:
            from illallangi.data.mastodon.adapters import (
                MastodonAdapter as DjangoAdapter,
            )

            src = MastodonAdapter(
                **settings.MASTODON,
            )
            dst = DjangoAdapter()

            src.load()
            dst.load()

            src.sync_to(dst)

        ModelsManager().add_synchronize(
            name=__name__,
            synchronize=synchronize,
        )
