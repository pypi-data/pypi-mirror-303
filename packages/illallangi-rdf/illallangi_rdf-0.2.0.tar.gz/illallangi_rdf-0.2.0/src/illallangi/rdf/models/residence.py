import diffsync
from partial_date import PartialDate


class Residence(diffsync.DiffSyncModel):
    label: str

    country: str
    finish: PartialDate | None
    locality: str
    olc: str
    postal_code: str
    region: str
    start: PartialDate | None
    street: str

    _modelname = "Residence"
    _identifiers = ("label",)
    _attributes = (
        "country",
        "finish",
        "locality",
        "olc",
        "postal_code",
        "region",
        "start",
        "street",
    )

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Residence":
        raise NotImplementedError

    def update(
        self,
        attrs: dict,
    ) -> "Residence":
        raise NotImplementedError

    def delete(
        self,
    ) -> "Residence":
        raise NotImplementedError
