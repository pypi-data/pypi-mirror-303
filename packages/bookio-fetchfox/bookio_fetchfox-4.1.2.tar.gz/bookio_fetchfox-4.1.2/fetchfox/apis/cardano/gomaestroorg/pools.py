from typing import Iterable, Tuple

from fetchfox.checks import check_str
from .common import get


def get_information(pool_id: str, api_key: str = None, preprod: bool = False) -> dict:
    check_str(pool_id, "gomaestroorg.pool_id")

    pool_id = pool_id.strip().lower()

    response, status_code = get(
        service=f"pools/{pool_id}/info",
        api_key=api_key,
        preprod=preprod,
    )

    return response["data"]


def get_delegators(pool_id: str, api_key: str = None, preprod: bool = False) -> Iterable[Tuple[str, float]]:
    check_str(pool_id, "gomaestroorg.pool_id")

    pool_id = pool_id.strip().lower()

    cursor = None

    while True:
        response, status_code = get(
            service=f"pools/{pool_id}/delegators",
            params={
                "cursor": cursor,
            },
            api_key=api_key,
            preprod=preprod,
        )

        for item in response.get("data", []):
            amount = item["amount"]

            if amount == 0:
                continue

            yield item["stake_address"], amount

        cursor = response.get("next_cursor")

        if not cursor:
            break
