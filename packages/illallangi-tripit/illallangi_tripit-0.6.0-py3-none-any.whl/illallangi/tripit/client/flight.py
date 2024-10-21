from collections.abc import Generator
from datetime import datetime, timezone
from typing import Any

import more_itertools

from illallangi.tripit.utils import try_jsonpatch

UNKNOWN = ""
BUSINESS_CLASS = "Business"
FIRST_CLASS = "First"
PREMIUM_ECONOMY = "Premium Economy"
ECONOMY = "Economy"

CLASSES = {
    "": UNKNOWN,
    "business saver": BUSINESS_CLASS,
    "business": BUSINESS_CLASS,
    "c": UNKNOWN,
    "discount business": BUSINESS_CLASS,
    "e": ECONOMY,
    "economy - e": ECONOMY,
    "economy - h": ECONOMY,
    "economy - k": ECONOMY,
    "economy - m": ECONOMY,
    "economy - n": ECONOMY,
    "economy - q": ECONOMY,
    "economy - s": ECONOMY,
    "economy - y": ECONOMY,
    "economy / k": ECONOMY,
    "economy": ECONOMY,
    "elevate": UNKNOWN,
    "f": FIRST_CLASS,
    "first": FIRST_CLASS,
    "flex y/b (y)": ECONOMY,
    "flex y/b": ECONOMY,
    "flex": UNKNOWN,
    "freedom": UNKNOWN,
    "h": ECONOMY,
    "i": UNKNOWN,
    "k": ECONOMY,
    "l": UNKNOWN,
    "m": ECONOMY,
    "n": ECONOMY,
    "premium economy": PREMIUM_ECONOMY,
    "q": ECONOMY,
    "red e-deal (q)": ECONOMY,
    "red e-deal": ECONOMY,
    "s": ECONOMY,
    "sale": UNKNOWN,
    "saver": UNKNOWN,
    "v": UNKNOWN,
    "y": ECONOMY,
}

TERMINALS = {
    UNKNOWN: UNKNOWN,
    "1": "Terminal 1",
    "2": "Terminal 2",
    "3": "Terminal 3",
    "4": "Terminal 4",
    "5": "Terminal 5",
    "6": "Terminal 6",
    "d": "Terminal D",
    "tbit": "Tom Bradley International",
    "a": "Terminal A",
    "b": "Terminal B",
    "c": "Terminal C",
    "intl": "International",
    "i": "International",
}


class FlightMixin:
    def get_flights(
        self,
    ) -> Generator[dict[str, Any], None, None]:
        for air in self.get_objects(
            "AirObject",
            self.base_url
            / "list"
            / "object"
            / "traveler"
            / "true"
            / "past"
            / "true"
            / "include_objects"
            / "false"
            / "type"
            / "air",
            self.base_url
            / "list"
            / "object"
            / "traveler"
            / "true"
            / "past"
            / "false"
            / "include_objects"
            / "false"
            / "type"
            / "air",
        ):
            for segment in [
                try_jsonpatch(
                    segment,
                    segment.get("notes"),
                )
                for segment in more_itertools.always_iterable(
                    air.get("Segment", []),
                    base_type=dict,
                )
            ]:
                yield {
                    "Airline": segment["marketing_airline_code"],
                    "Arrival": datetime.fromisoformat(
                        f'{segment["EndDateTime"]["date"]}T{segment["EndDateTime"]["time"]}{segment["EndDateTime"]["utc_offset"]}',
                    ).astimezone(timezone.utc),
                    "ArrivalTimeZone": segment["EndDateTime"]["timezone"],
                    "Departure": datetime.fromisoformat(
                        f'{segment["StartDateTime"]["date"]}T{segment["StartDateTime"]["time"]}{segment["StartDateTime"]["utc_offset"]}',
                    ).astimezone(timezone.utc),
                    "DepartureTimeZone": segment["StartDateTime"]["timezone"],
                    "Destination": segment.get("end_airport_code"),
                    "DestinationCity": segment["end_city_name"],
                    "DestinationTerminal": TERMINALS[
                        segment.get("end_terminal", "").lower()
                    ],
                    "DestinationGate": segment.get("end_gate", ""),
                    "FlightClass": CLASSES[segment.get("service_class", "").lower()],
                    "FlightNumber": f'{segment["marketing_airline_code"]}{segment["marketing_flight_number"].rjust(4, " ")}',
                    "Origin": segment.get("start_airport_code", ""),
                    "OriginCity": segment["start_city_name"],
                    "OriginTerminal": TERMINALS[
                        segment.get("start_terminal", "").lower()
                    ],
                    "OriginGate": segment.get("start_gate", ""),
                    "SequenceNumber": segment["id"][-3:],
                    "Seat": segment.get("seats", "").lstrip("0"),
                    "Passenger": ", ".join(
                        [
                            name
                            for name in [
                                more_itertools.first(
                                    more_itertools.always_iterable(
                                        air.get("Traveler", [{}]), base_type=dict
                                    )
                                ).get("last_name"),
                                " ".join(
                                    [
                                        name
                                        for name in [
                                            more_itertools.first(
                                                more_itertools.always_iterable(
                                                    air.get("Traveler", [{}]),
                                                    base_type=dict,
                                                )
                                            ).get("first_name"),
                                            more_itertools.first(
                                                more_itertools.always_iterable(
                                                    air.get("Traveler", [{}]),
                                                    base_type=dict,
                                                )
                                            ).get("middle_name"),
                                        ]
                                        if name
                                    ],
                                ),
                            ]
                            if name
                        ]
                    ),
                    "@air": {
                        k: v for k, v in air.items() if k not in ["@api", "Segment"]
                    },
                    "@api": air["@api"],
                    "@segment": segment,
                }
