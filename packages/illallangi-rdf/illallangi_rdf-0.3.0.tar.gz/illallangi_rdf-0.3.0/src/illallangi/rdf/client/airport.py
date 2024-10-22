class AirportMixin:
    def get_airports_query(
        self,
        airport_iata: list[str],
    ) -> str:
        return f"""
SELECT ?label ?iata ?icao WHERE {{
    VALUES (?value) {{ ( "{'" ) ( "'.join([i.upper() for i in airport_iata])}" ) }}
    ?href ip:airportIataCode ?value.
    ?href rdfs:label ?label .
    ?href ip:airportIataCode ?iata .
    ?href ip:airportIcaoCode ?icao .
    ?href a ic:airport .
}}
"""

    def get_airports(
        self,
        *_args: list,
        airport_iata: list[str] | None = None,
        **_kwargs: dict,
    ) -> list[dict]:
        if airport_iata is None:
            return []

        result = self.graph.query(
            self.get_airports_query(
                airport_iata=airport_iata,
            ),
        )

        return [
            {str(k): str(b[str(k)]) if str(k) in b else None for k in result.vars}
            for b in result.bindings
        ]
