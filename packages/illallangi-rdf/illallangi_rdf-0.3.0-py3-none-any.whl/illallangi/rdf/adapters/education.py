from typing import ClassVar

import diffsync

from illallangi.rdf import RDFClient
from illallangi.rdf.models import Course


class EducationAdapter(diffsync.Adapter):
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

    Course = Course

    top_level: ClassVar = [
        "Course",
    ]

    type = "rdf_education"

    def load(
        self,
        *args: list,
        **kwargs: dict,
    ) -> None:
        for obj in self.client.get_courses(
            *args,
            **kwargs,
        ):
            self.add(
                Course(
                    label=obj["label"],
                    country=obj["country"],
                    finish=obj["finish"],
                    institution=obj["institution"],
                    locality=obj["locality"],
                    olc=obj["olc"],
                    postal_code=obj["postal_code"],
                    region=obj["region"],
                    start=obj["start"],
                    street=obj["street"],
                ),
            )
