from datetime import date

import diffsync

from illallangi.data.fitness.models.swim import Swim as ModelSwim


class Swim(
    diffsync.DiffSyncModel,
):
    pk: int
    url: str
    date: date
    distance: int
    laps: float

    _modelname = "Swim"
    _identifiers = ("url",)
    _attributes = (
        "date",
        "distance",
        "laps",
    )

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Swim":
        obj = ModelSwim.objects.update_or_create(
            url=ids["url"],
            defaults={
                "date": attrs["date"],
                "distance": attrs["distance"],
                "laps": attrs["laps"],
            },
        )[0]

        return super().create(
            adapter,
            {
                "pk": obj.pk,
                **ids,
            },
            attrs,
        )

    def update(
        self,
        attrs: dict,
    ) -> "Swim":
        ModelSwim.objects.filter(
            pk=self.pk,
        ).update(
            **attrs,
        )

        return super().update(attrs)

    def delete(
        self,
    ) -> "Swim":
        ModelSwim.objects.get(
            pk=self.pk,
        ).delete()

        return super().delete()
