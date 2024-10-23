import json
from base64 import b64decode
from functools import lru_cache
from typing import Iterable

from fetchfox.checks import check_str
from .common import get


@lru_cache(maxsize=None)
def get_data(asset_id: str) -> dict:
    check_str(asset_id, "algonodecloud.asset_id")

    response, status_code = get(
        service=f"assets/{asset_id}",
    )

    return response["asset"]["params"]


@lru_cache(maxsize=None)
def get_metadata(asset_id: str) -> dict:
    check_str(asset_id, "algonodecloud.asset_id")

    response, status_code = get(
        f"assets/{asset_id}/transactions",
        params={
            "tx-type": "acfg",
            "limit": "1",
        },
    )

    transaction = response["transactions"][0]

    if "note" in transaction:
        note = b64decode(transaction["note"]).decode("utf-8")
    else:
        note = "{}"

    return json.loads(note)


def get_holders(asset_id: str) -> Iterable[dict]:
    check_str(asset_id, "algonodecloud.asset_id")

    response, status_code = get(
        service=f"assets/{asset_id}/balances",
        params={
            "currency-greater-than": "0",
        },
    )

    balances = response.get("balances", [])

    if not balances:
        yield None

    yield {
        "asset_id": asset_id,
        "address": balances[0]["address"],
        "amount": balances[0]["amount"],
    }
