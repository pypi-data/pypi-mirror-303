from functools import lru_cache
from typing import Iterable

from fetchfox.checks import check_str
from .common import get


def get_holders(asset_id: str, api_key: str = None, preprod: bool = False) -> Iterable[dict]:
    check_str(asset_id, "gomaestroorg.asset_id")

    cursor = None

    while True:
        response, status_code = get(
            service=f"assets/{asset_id}/accounts",
            params={
                "cursor": cursor,
            },
            api_key=api_key,
            preprod=preprod,
        )

        for item in response.get("data", []):
            yield {
                "asset_id": asset_id,
                "stake_address": item["account"],
                "amount": int(item["amount"]),
            }

        cursor = response.get("next_cursor")

        if not cursor:
            break


@lru_cache(maxsize=None)
def get_data(asset_id: str, api_key: str = None, preprod: bool = False) -> dict:
    check_str(asset_id, "gomaestroorg.asset_id")

    asset_id = asset_id.strip().lower()

    response, status_code = get(
        service=f"assets/{asset_id}",
        api_key=api_key,
        preprod=preprod,
    )

    cip25_metadata = response["data"]["asset_standards"].get("cip25_metadata")
    cip68_metadata = response["data"]["asset_standards"].get("cip68_metadata")

    metadata = cip68_metadata or cip25_metadata
    metadata["total_supply"] = response["data"].get("total_supply", "1")

    return metadata
