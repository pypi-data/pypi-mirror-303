from autoslug import AutoSlugField
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django_sqids import SqidsField


class Alliance(
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

    name = models.CharField(  # noqa: DJ001
        blank=True,
        max_length=255,
        null=True,
    )

    # Methods

    def __str__(
        self,
    ) -> str:
        return self.name

    def get_absolute_url(
        self,
    ) -> str:
        return reverse(
            "alliance_html",
            kwargs={
                "alliance_slug": self.slug,
            },
        )

    def get_logo_url(
        self,
    ) -> str:
        return static(f"aviation/alliance_logos/{self.slug}.png")

    def get_slug(
        self,
    ) -> str:
        return self.name
