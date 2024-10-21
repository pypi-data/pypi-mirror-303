from partial_date import PartialDate


class ResidenceMixin:
    def get_residences_query(
        self,
        rdf_root: str,
    ) -> str:
        return f"""
PREFIX i: <http://data.coley.au/rdf/entity#>
PREFIX ip: <http://data.coley.au/rdf/property#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX v: <http://www.w3.org/2006/vcard/ns#>


SELECT ?start ?finish ?label ?street ?locality ?region ?postal_code ?country ?olc WHERE {{
    <{ rdf_root }> ip:residedAt ?residedAt .
    OPTIONAL {{ ?residedAt ip:startTime ?start }} .
    OPTIONAL {{ ?residedAt ip:endTime ?finish }} .
    ?residedAt ip:atResidence ?atResidence .

    OPTIONAL {{ ?atResidence rdfs:label ?label . }}

    OPTIONAL {{ ?atResidence v:Address ?address
        OPTIONAL {{ ?address v:street-address ?street }}
        OPTIONAL {{ ?address v:locality ?locality }}
        OPTIONAL {{ ?address v:region ?region }}
        OPTIONAL {{ ?address v:postal-code ?postal_code }}
        OPTIONAL {{ ?address v:country-name ?country }}
    }}
    OPTIONAL {{ ?atResidence ip:olc ?olc }} .
}}
"""

    def get_residences(
        self,
        *args: list,
        **kwargs: dict,
    ) -> list[dict]:
        result = self.graph.query(
            self.get_residences_query(
                *args,
                **kwargs,
            ),
        )

        return sorted(
            [
                {
                    **{
                        str(k): b[str(k)].value if str(k) in b else None
                        for k in result.vars
                    },
                    "start": PartialDate(b["start"].value)
                    if "start" in b and b["start"].value not in ["Unknown"]
                    else None,
                    "finish": PartialDate(b["finish"].value)
                    if "finish" in b and b["finish"].value not in ["Unknown"]
                    else None,
                }
                for b in result.bindings
            ],
            key=lambda x: str(x["start"]),
        )
