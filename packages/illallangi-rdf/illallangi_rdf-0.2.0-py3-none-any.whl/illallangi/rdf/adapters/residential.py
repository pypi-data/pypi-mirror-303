from typing import ClassVar

import diffsync

from illallangi.rdf import RDFClient
from illallangi.rdf.models import Residence


class ResidentialAdapter(diffsync.Adapter):
    def __init__(
        self,
        *args: list,
        **kwargs: dict,
    ) -> None:
        super().__init__()
        self.client = RDFClient(
            *args,
            **kwargs,
        )

    Residence = Residence

    top_level: ClassVar = [
        "Residence",
    ]

    type = "rdf_residential"

    def load(
        self,
        *args: list,
        **kwargs: dict,
    ) -> None:
        for obj in self.client.get_residences(
            *args,
            **kwargs,
        ):
            self.add(
                Residence(
                    country=obj["country"],
                    finish=obj["finish"],
                    label=obj["label"],
                    locality=obj["locality"],
                    olc=obj["olc"],
                    postal_code=obj["postal_code"],
                    region=obj["region"],
                    start=obj["start"],
                    street=obj["street"],
                ),
            )
