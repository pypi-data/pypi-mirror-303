from datetime import datetime

import diffsync

from illallangi.data.air_transport.models import Trip as ModelTrip


class Trip(
    diffsync.DiffSyncModel,
):
    _modelname = "Trip"
    _identifiers = (
        "start",
        "name",
    )
    _attributes = ("end",)

    pk: int

    start: datetime
    name: str

    end: datetime

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Trip":
        obj = ModelTrip.objects.update_or_create(
            start=ids["start"],
            name=ids["name"],
            defaults={
                "end": attrs["end"],
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
    ) -> "Trip":
        ModelTrip.objects.filter(
            pk=self.pk,
        ).update(
            **attrs,
        )

        return super().update(attrs)

    def delete(
        self,
    ) -> "Trip":
        ModelTrip.objects.get(
            pk=self.pk,
        ).delete()

        return super().delete()
