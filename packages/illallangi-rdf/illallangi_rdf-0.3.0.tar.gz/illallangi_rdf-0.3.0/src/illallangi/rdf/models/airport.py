import diffsync


class Airport(diffsync.DiffSyncModel):
    iata: str

    label: str
    icao: str

    _modelname = "Airport"
    _identifiers = ("iata",)
    _attributes = (
        "label",
        "icao",
    )

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Airport":
        raise NotImplementedError

    def update(
        self,
        attrs: dict,
    ) -> "Airport":
        raise NotImplementedError

    def delete(
        self,
    ) -> "Airport":
        raise NotImplementedError
