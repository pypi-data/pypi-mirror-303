from django.apps import AppConfig
from django.conf import settings

from illallangi.django.data.models.models_manager import ModelsManager
from illallangi.rdf.adapters import ResidentialAdapter as RDFAdapter


class ResidentialHistoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "illallangi.data.residential"

    def ready(self) -> None:
        ModelsManager().add_model(
            singular="Residence",
            plural="Residences",
            model="illallangi.data.residential.models.Residence",
            url="residences_html",
            icon="residential/residences.jpg",
            description="Not just a location on a map, but a place where dreams are nurtured and memories are made.",
        )

        def synchronize() -> None:
            from illallangi.data.residential.adapters import (
                ResidentialAdapter as DjangoAdapter,
            )

            src = RDFAdapter(
                **settings.RDF,
            )
            dst = DjangoAdapter()

            src.load(
                **settings.RESIDENTIAL,
            )
            dst.load()

            src.sync_to(dst)

        ModelsManager().add_synchronize(
            name=__name__,
            synchronize=synchronize,
        )
