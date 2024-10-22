from typing import ClassVar

import diffsync

from illallangi.rdf import RDFClient
from illallangi.rdf.models import Airline, Airport


class AviationAdapter(diffsync.Adapter):
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

    Airline = Airline
    Airport = Airport

    top_level: ClassVar = [
        "Airline",
        "Airport",
    ]

    type = "rdf_aviation"

    def load(
        self,
        *args: list,
        **kwargs: dict,
    ) -> None:
        for obj in self.client.get_airlines(
            *args,
            **kwargs,
        ):
            self.add(
                Airline(
                    iata=obj["iata"],
                    label=obj["label"],
                    icao=obj["icao"],
                    alliance=obj["alliance"],
                    dominant_color=obj["dominant_color"],
                ),
            )

        for obj in self.client.get_airports(
            *args,
            **kwargs,
        ):
            self.add(
                Airport(
                    iata=obj["iata"],
                    label=obj["label"],
                    icao=obj["icao"],
                ),
            )
