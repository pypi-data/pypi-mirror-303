from django.apps import AppConfig
from django.conf import settings

from illallangi.django.data.models.models_manager import ModelsManager
from illallangi.rdf.adapters import AviationAdapter as RDFAdapter


class AviationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "illallangi.data.aviation"

    def ready(self) -> None:
        ModelsManager().add_model(
            description="Alliances of airlines working together to provide a seamless travel experience.",
            icon="aviation/alliances.jpg",
            model="illallangi.data.aviation.models.Alliance",
            plural="Alliances",
            singular="Alliance",
            url="alliances_html",
        )
        ModelsManager().add_model(
            description="Connecting us to the world, turning dreams of distant places into reality and reminding us that the sky holds endless adventures.",
            icon="aviation/airlines.jpg",
            model="illallangi.data.aviation.models.Airline",
            plural="Airlines",
            singular="Airline",
            url="airlines_html",
        )
        ModelsManager().add_model(
            description="Gateways to endless possibilities, where every departure is the start of a new adventure and every arrival is a homecoming.",
            icon="aviation/airports.jpg",
            model="illallangi.data.aviation.models.Airport",
            plural="Airports",
            singular="Airport",
            url="airports_html",
        )

        def synchronize() -> None:
            from illallangi.data.aviation.adapters import (
                AviationAdapter as DjangoAdapter,
            )
            from illallangi.data.aviation.models import Airline, Airport

            src = RDFAdapter(
                **settings.RDF,
            )
            dst = DjangoAdapter()

            src.load(
                airline_iata=[airline.iata for airline in Airline.objects.all()],
                airport_iata=[airport.iata for airport in Airport.objects.all()],
                **settings.AVIATION,
            )
            dst.load()

            src.sync_to(dst)

        ModelsManager().add_synchronize(
            name=__name__,
            synchronize=synchronize,
            before=[
                "illallangi.data.air_transport.apps",
            ],
        )
