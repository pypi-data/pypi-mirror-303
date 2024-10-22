from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django_sqids import SqidsField


class Status(
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

    content = models.TextField(
        null=False,
        blank=False,
    )

    datetime = models.DateTimeField(
        null=False,
        blank=False,
    )

    # Methods

    def __str__(
        self,
    ) -> str:
        return f"Status {self.id}"

    def get_absolute_url(
        self,
    ) -> str:
        return reverse(
            "status_html",
            kwargs={
                "status_slug": self.sqid,
                "status_year": str(self.datetime.year).zfill(4),
                "status_month": str(self.datetime.month).zfill(2),
                "status_day": str(self.datetime.day).zfill(2),
            },
        )

    def get_slug(
        self,
    ) -> str:
        return self.sqid
