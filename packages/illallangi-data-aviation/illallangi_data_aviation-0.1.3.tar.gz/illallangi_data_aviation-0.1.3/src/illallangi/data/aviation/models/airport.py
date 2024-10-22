from autoslug import AutoSlugField
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django_sqids import SqidsField


class Airport(
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

    # ip:airlineIataCode: "Airport IATA Code"
    # P238: IATA airport code
    iata = models.CharField(
        blank=False,
        help_text="three-letter identifier for designating airports",
        max_length=3,
        null=False,
        unique=True,
        verbose_name="IATA airport code",
    )

    # Fields

    # ip:airlineIataCode: "Airport ICAO Code"
    # P239: ICAO airport code
    icao = models.CharField(  # noqa: DJ001
        blank=True,
        help_text="four-character alphanumeric identifier for designating airports",
        max_length=4,
        null=True,
        verbose_name="ICAO airport code",
    )

    # rdfs:label: "A human-readable name for the subject"
    label = models.CharField(  # noqa: DJ001
        blank=True,
        help_text="A human-readable name for the subject",
        max_length=255,
        null=True,
        verbose_name="Label",
    )

    # Methods

    def __str__(
        self,
    ) -> str:
        if self.label:
            return self.label
        return self.iata

    def get_absolute_url(
        self,
    ) -> str:
        return reverse(
            "airport_html",
            kwargs={
                "airport_slug": self.slug,
            },
        )

    def get_logo_url(
        self,
    ) -> str:
        return static(f"aviation/airport_logos/{self.slug}.png")

    def get_slug(
        self,
    ) -> str:
        if self.label:
            return self.label
        return self.iata
