from typing import ClassVar

import diffsync

from illallangi.data.residential.diffsyncmodels import Residence
from illallangi.data.residential.models import Residence as DjangoResidence


class ResidentialAdapter(diffsync.Adapter):
    Residence = Residence

    top_level: ClassVar = [
        "Residence",
    ]

    type = "django_residential"

    def load(
        self,
    ) -> None:
        if self.count() > 0:
            return

        for obj in DjangoResidence.objects.all():
            self.add(
                Residence(
                    pk=obj.pk,
                    label=obj.label,
                    country=obj.country,
                    finish=obj.finish,
                    locality=obj.locality,
                    olc=obj.olc,
                    postal_code=obj.postal_code,
                    region=obj.region,
                    start=obj.start,
                    street=obj.street,
                ),
            )
