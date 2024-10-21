from partial_date import PartialDate


class CourseMixin:
    def get_courses_query(
        self,
        rdf_root: str,
    ) -> str:
        return f"""
SELECT ?start ?finish ?label ?institution ?street ?locality ?region ?postal_code ?country ?olc WHERE {{
    <{ rdf_root }> ip:attendedCourse ?attended_course .
    OPTIONAL {{ ?attended_course ip:startTime ?start }} .
    OPTIONAL {{ ?attended_course ip:endTime ?finish }} .
    ?attended_course rdfs:label ?label .
    ?attended_course ip:atInstitution ?at_institution .

    OPTIONAL {{ ?at_institution rdfs:label ?institution . }}

    OPTIONAL {{ ?at_institution v:Address ?address
        OPTIONAL {{ ?address v:street-address ?street }}
        OPTIONAL {{ ?address v:locality ?locality }}
        OPTIONAL {{ ?address v:region ?region }}
        OPTIONAL {{ ?address v:postal-code ?postal_code }}
        OPTIONAL {{ ?address v:country-name ?country }}
    }}
    OPTIONAL {{ ?at_institution ip:olc ?olc }} .
}}
"""

    def get_courses(
        self,
        *args: list,
        **kwargs: dict,
    ) -> list[dict]:
        result = self.graph.query(
            self.get_courses_query(
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
