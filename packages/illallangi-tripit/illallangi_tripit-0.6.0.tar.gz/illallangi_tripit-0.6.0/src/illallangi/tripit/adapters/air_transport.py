from typing import ClassVar

import diffsync

from illallangi.tripit import TripItClient
from illallangi.tripit.diffsyncmodels import Flight, Trip


class AirTransportAdapter(diffsync.Adapter):
    def __init__(
        self,
        *args: list,
        **kwargs: dict,
    ) -> None:
        super().__init__()
        self.client = TripItClient(
            *args,
            **kwargs,
        )

    Flight = Flight
    Trip = Trip

    top_level: ClassVar = [
        "Flight",
        "Trip",
    ]

    type = "tripit_air_transport"

    def load(
        self,
        *args: list,
        **kwargs: dict,
    ) -> None:
        for obj in self.client.get_flights(
            *args,
            **kwargs,
        ):
            self.add(
                Flight(
                    airline=obj["Airline"],
                    arrival=obj["Arrival"],
                    arrival_timezone=obj["ArrivalTimeZone"],
                    departure=obj["Departure"],
                    departure_timezone=obj["DepartureTimeZone"],
                    destination=obj["Destination"],
                    destination_city=obj["DestinationCity"],
                    destination_gate=obj["DestinationGate"],
                    destination_terminal=obj["DestinationTerminal"],
                    flight_class=obj["FlightClass"],
                    flight_number=obj["FlightNumber"],
                    origin=obj["Origin"],
                    origin_city=obj["OriginCity"],
                    origin_gate=obj["OriginGate"],
                    origin_terminal=obj["OriginTerminal"],
                    passenger=obj["Passenger"],
                    seat=obj["Seat"],
                    sequence_number=obj["SequenceNumber"],
                ),
            )
        for obj in self.client.get_trips(
            *args,
            **kwargs,
        ):
            self.add(
                Trip(
                    end=obj["End"],
                    name=obj["Name"],
                    start=obj["Start"],
                ),
            )
