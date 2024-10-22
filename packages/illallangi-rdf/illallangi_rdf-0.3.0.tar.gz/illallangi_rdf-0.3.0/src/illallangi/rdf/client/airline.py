class AirlinesNotFoundError(Exception):
    def __init__(
        self,
        airline_iata: list[str],
    ) -> None:
        self.airline_iata = airline_iata
        msg = f"Airline(s) not found: {', '.join(airline_iata)}"
        super().__init__(msg)


class AirlineMixin:
    def get_airlines_query(
        self,
        airline_iata: list[str],
    ) -> str:
        return f"""
    SELECT ?label ?iata ?icao ?alliance ?dominant_color WHERE {{
        VALUES (?value) {{ ( "{'" ) ( "'.join(airline_iata)}" ) }}
        ?href ip:airlineIataCode ?value.
        ?href rdfs:label ?label .
        ?href ip:airlineIataCode ?iata .
        OPTIONAL {{ ?href ip:airlineIcaoCode ?icao . }}
        OPTIONAL {{
            ?href ip:memberOfAirlineAlliance ?allianceHref .
            ?allianceHref rdfs:label ?alliance .
        }}
        OPTIONAL {{ ?href ip:dominantColor ?dominant_color . }}
        ?href a ic:airline .
    }}
    """

    def get_airlines(
        self,
        *_args: list,
        airline_iata: list[str] | None = None,
        **_kwargs: dict,
    ) -> list[dict]:
        if airline_iata is None:
            return []
        airline_iata = [i.upper() for i in airline_iata]

        result = self.graph.query(
            self.get_airlines_query(
                airline_iata=airline_iata,
            ),
        )

        result = [
            {str(k): str(b[str(k)]) if str(k) in b else None for k in result.vars}
            for b in result.bindings
        ]

        not_found = [i for i in airline_iata if i not in [j["iata"] for j in result]]
        if not_found:
            raise AirlinesNotFoundError(not_found)

        return result
