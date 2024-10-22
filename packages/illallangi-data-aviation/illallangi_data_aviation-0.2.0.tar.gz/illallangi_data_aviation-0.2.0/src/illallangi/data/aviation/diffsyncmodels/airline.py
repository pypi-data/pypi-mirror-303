import diffsync

from illallangi.data.aviation.models import Airline as ModelAirline
from illallangi.data.aviation.models import Alliance


class Airline(diffsync.DiffSyncModel):
    pk: int
    iata: str

    label: str | None
    icao: str | None
    alliance: str | None
    dominant_color: str | None

    _modelname = "Airline"
    _identifiers = ("iata",)
    _attributes = (
        "label",
        "icao",
        "alliance",
        "dominant_color",
    )

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Airline":
        alliance = (
            Alliance.objects.get_or_create(name=attrs["alliance"])[0]
            if "alliance" in attrs and attrs["alliance"] is not None
            else None
        )

        obj = ModelAirline.objects.update_or_create(
            iata=ids["iata"],
            defaults={
                "label": attrs["label"],
                "icao": attrs["icao"],
                "alliance": alliance,
                "dominant_color": attrs["dominant_color"],
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
    ) -> "Airline":
        alliance = (
            Alliance.objects.get_or_create(name=attrs["alliance"])[0]
            if "alliance" in attrs and attrs["alliance"] is not None
            else None
        )

        ModelAirline.objects.filter(
            pk=self.pk,
        ).update(
            **{
                **attrs,
                "alliance": alliance,
            },
        )

        return super().update(attrs)

    def delete(
        self,
    ) -> "Airline":
        ModelAirline.objects.get(
            pk=self.pk,
        ).delete()

        return super().delete()
