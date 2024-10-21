import diffsync


class Airline(diffsync.DiffSyncModel):
    iata: str

    label: str
    icao: str | None
    alliance: str | None

    _modelname = "Airline"
    _identifiers = ("iata",)
    _attributes = (
        "label",
        "icao",
        "alliance",
    )

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Airline":
        raise NotImplementedError

    def update(
        self,
        attrs: dict,
    ) -> "Airline":
        raise NotImplementedError

    def delete(
        self,
    ) -> "Airline":
        raise NotImplementedError
