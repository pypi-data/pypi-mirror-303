from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django_sqids import SqidsField
from partial_date import PartialDateField


class Residence(
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

    # Natural Keys

    label = models.CharField(
        max_length=63,
        null=False,
        blank=False,
        unique=True,
    )

    # Fields

    country = models.CharField(
        max_length=63,
    )

    finish = PartialDateField(
        null=True,
        blank=True,
    )

    locality = models.CharField(
        max_length=63,
    )

    olc = models.CharField(
        max_length=11,
    )

    postal_code = models.CharField(
        max_length=63,
    )

    region = models.CharField(
        max_length=63,
    )

    start = PartialDateField(
        null=True,
        blank=True,
    )

    street = models.CharField(
        max_length=63,
    )

    # Methods

    def __str__(
        self,
    ) -> str:
        return self.label

    def get_absolute_url(
        self,
    ) -> str:
        return reverse(
            "residence_html",
            kwargs={
                "residence_slug": self.slug,
            },
        )

    def get_olc_url(
        self,
    ) -> str:
        if not self.olc:
            return None
        return f"https://plus.codes/{self.olc}"

    def get_slug(
        self,
    ) -> str:
        return self.label
