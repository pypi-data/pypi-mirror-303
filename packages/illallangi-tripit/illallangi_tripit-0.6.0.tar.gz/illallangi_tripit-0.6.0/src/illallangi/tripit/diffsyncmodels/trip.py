from datetime import datetime

import diffsync


class Trip(diffsync.DiffSyncModel):
    _modelname = "Trip"
    _identifiers = (
        "start",
        "name",
    )
    _attributes = ("end",)

    end: datetime
    name: str
    start: datetime

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Trip":
        raise NotImplementedError

    def update(
        self,
        attrs: dict,
    ) -> "Trip":
        raise NotImplementedError

    def delete(
        self,
    ) -> "Trip":
        raise NotImplementedError
