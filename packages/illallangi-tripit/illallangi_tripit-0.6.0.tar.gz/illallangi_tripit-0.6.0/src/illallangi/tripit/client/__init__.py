import datetime
import sys
from collections.abc import Generator
from pathlib import Path
from queue import Queue
from typing import Any

import more_itertools
from alive_progress import alive_bar
from appdirs import user_config_dir
from requests_cache import CacheMixin
from requests_oauthlib import OAuth1Session
from yarl import URL

from illallangi.tripit.__version__ import __version__
from illallangi.tripit.client.flight import FlightMixin
from illallangi.tripit.client.profile import ProfileMixin
from illallangi.tripit.client.trip import TripMixin

CACHE_NAME = Path(user_config_dir()) / "illallangi-tripit.db"


class Session(
    CacheMixin,
    OAuth1Session,
):
    pass


def try_float(
    value: str,
) -> float | str:
    try:
        return float(value)
    except (ValueError, TypeError):
        return value


class TripItClient(
    FlightMixin,
    ProfileMixin,
    TripMixin,
):
    def __init__(
        self,
        tripit_access_token: str,
        tripit_access_token_secret: str,
        tripit_client_token: str,
        tripit_client_token_secret: str,
        base_url: URL = "https://api.tripit.com/v1",
    ) -> None:
        if not isinstance(base_url, URL):
            base_url = URL(base_url)

        self.base_url = base_url

        self._session = Session(
            client_key=tripit_client_token,
            client_secret=tripit_client_token_secret,
            resource_owner_key=tripit_access_token,
            resource_owner_secret=tripit_access_token_secret,
            cache_name=CACHE_NAME,
            backend="sqlite",
            expire_after=3600,
        )

    def get_info(
        self,
    ) -> dict:
        return {
            "returned": int(datetime.datetime.now(tz=datetime.UTC).timestamp()),
            "version": __version__,
        }

    def get_objects(
        self,
        key: str,
        *args: URL,
    ) -> Generator[dict[str, Any], None, None]:
        queue = Queue()
        seen = set()

        for arg in args:
            seen.add(
                arg
                % {
                    "format": "json",
                    "page_size": 13,
                    "page_num": 1,
                }
            )
            queue.put(
                arg
                % {
                    "format": "json",
                    "page_size": 13,
                    "page_num": 1,
                }
            )

        with alive_bar(
            manual=True,
            file=sys.stderr,
        ) as bar:
            while not queue.empty():
                url = queue.get()
                bar.text(f"{url.human_repr()}; {queue.qsize()} to go.")

                response = self._session.get(url)

                response.raise_for_status()

                json = response.json()

                yield from [
                    {
                        **o,
                        "@api": {
                            **{
                                k: try_float(v)
                                for k, v in json.items()
                                if k
                                not in [
                                    "AirObject",
                                    "Profile",
                                    "Trip",
                                ]
                            },
                            "from_cache": response.from_cache,
                            "expires": int(response.expires.timestamp()),
                            "url": url.human_repr(),
                            **self.get_info(),
                        },
                    }
                    for o in more_itertools.always_iterable(
                        json.get(key, []),
                        base_type=dict,
                    )
                ]

                if "max_page" in json:
                    for page_num in range(
                        1,
                        int(json["max_page"]) + 1,
                    ):
                        u = url % {
                            "format": "json",
                            "page_size": 13,
                            "page_num": page_num,
                        }
                        if u in seen:
                            continue
                        seen.add(u)
                        queue.put(u)
                bar((len(seen) - queue.qsize()) / len(seen))
