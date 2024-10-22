from typing import ClassVar

import diffsync

from illallangi.data.aviation.diffsyncmodels import (
    Airline,
    Airport,
)
from illallangi.data.aviation.models import Airline as DjangoAirline
from illallangi.data.aviation.models import Airport as DjangoAirport


class AviationAdapter(diffsync.Adapter):
    Airline = Airline
    Airport = Airport

    top_level: ClassVar = [
        "Airline",
        "Airport",
    ]

    type = "django_aviation"

    def load(
        self,
    ) -> None:
        if self.count() > 0:
            return

        for obj in DjangoAirline.objects.all():
            self.add(
                Airline(
                    pk=obj.pk,
                    iata=obj.iata,
                    label=obj.label,
                    icao=obj.icao,
                    alliance=None if obj.alliance is None else obj.alliance.name,
                    dominant_color=obj.dominant_color,
                ),
            )

        for obj in DjangoAirport.objects.all():
            self.add(
                Airport(
                    pk=obj.pk,
                    iata=obj.iata,
                    label=obj.label,
                    icao=obj.icao,
                ),
            )
