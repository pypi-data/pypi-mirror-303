from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django_sqids import SqidsField


class Swim(
    models.Model,
):
    # Surrogate Keys

    id = models.AutoField(
        primary_key=True,
    )

    slug = AutoSlugField(
        populate_from="get_slug",
        unique=True,
    )

    sqid = SqidsField(
        real_field_name="id",
        min_length=6,
    )

    # Fields

    url = models.URLField(
        null=False,
        blank=False,
        unique=True,
    )

    date = models.DateField(
        null=False,
        blank=False,
    )

    distance = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    laps = models.FloatField(
        null=False,
        blank=False,
    )

    # Methods

    def __str__(
        self,
    ) -> str:
        return f"{self.distance}m Swim"

    def get_absolute_url(
        self,
    ) -> str:
        return reverse(
            "swim_html",
            kwargs={
                "swim_slug": self.sqid,
                "swim_year": str(self.date.year).zfill(4),
                "swim_month": str(self.date.month).zfill(2),
                "swim_day": str(self.date.day).zfill(2),
            },
        )

    def get_slug(
        self,
    ) -> str:
        return self.sqid
