from django.apps import AppConfig

from illallangi.django.data.models.models_manager import ModelsManager


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

        ModelsManager().add_synchronize(
            name=__name__,
            synchronize=None,
        )
