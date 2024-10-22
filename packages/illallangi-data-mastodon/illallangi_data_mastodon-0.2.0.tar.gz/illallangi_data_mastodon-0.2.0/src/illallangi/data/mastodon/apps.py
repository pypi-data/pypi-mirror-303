from django.apps import AppConfig

from illallangi.django.data.models.models_manager import ModelsManager


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

        ModelsManager().add_synchronize(
            name=__name__,
            synchronize=None,
        )
