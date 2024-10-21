from datetime import datetime

import diffsync


class Flight(diffsync.DiffSyncModel):
    _modelname = "Flight"
    _identifiers = (
        "departure",
        "flight_number",
    )
    _attributes = (
        "airline",
        "arrival",
        "arrival_timezone",
        "departure_timezone",
        "destination",
        "destination_city",
        "destination_gate",
        "destination_terminal",
        "flight_class",
        "origin",
        "origin_city",
        "origin_gate",
        "origin_terminal",
        "passenger",
        "seat",
        "sequence_number",
    )

    airline: str
    arrival: datetime
    arrival_timezone: str
    departure: datetime
    departure_timezone: str
    destination: str
    destination_city: str
    destination_gate: str
    destination_terminal: str
    flight_class: str
    flight_number: str
    origin: str
    origin_city: str
    origin_gate: str
    origin_terminal: str
    passenger: str
    seat: str
    sequence_number: str

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Flight":
        raise NotImplementedError

    def update(
        self,
        attrs: dict,
    ) -> "Flight":
        raise NotImplementedError

    def delete(
        self,
    ) -> "Flight":
        raise NotImplementedError
