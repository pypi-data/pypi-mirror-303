import contextlib

import jsonpatch


def try_jsonpatch(
    data: dict,
    patch: str,
) -> dict:
    if not patch:
        return data
    with contextlib.suppress(Exception):
        data = jsonpatch.JsonPatch.from_string(patch).apply(data)
    return data
