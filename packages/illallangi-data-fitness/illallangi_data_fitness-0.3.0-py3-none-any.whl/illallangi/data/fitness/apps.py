from django.apps import AppConfig
from django.conf import settings

from illallangi.django.data.models.models_manager import ModelsManager
from illallangi.mastodon.adapters import FitnessAdapter as MastodonAdapter


class MastodonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "illallangi.data.fitness"

    def ready(self) -> None:
        ModelsManager().add_model(
            singular="Swim",
            plural="Swims",
            model="illallangi.data.fitness.models.swim.Swim",
            url="swims_html",
            icon="fitness/swims.png",
            description="Swimming is a fantastic way to improve overall fitness and well-being.",
        )

        def synchronize() -> None:
            from illallangi.data.fitness.adapters import (
                FitnessAdapter as DjangoAdapter,
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
