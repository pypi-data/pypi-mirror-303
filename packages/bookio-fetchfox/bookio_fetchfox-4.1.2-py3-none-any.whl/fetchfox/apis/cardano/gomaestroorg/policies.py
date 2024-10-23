from typing import Iterable

from fetchfox.checks import check_str
from .common import get


def get_holders(policy_id: str, api_key: str = None, preprod: bool = False) -> Iterable[dict]:
    check_str(policy_id, "gomaestroorg.policy_id")
    policy_id = policy_id.strip().lower()

    cursor = None

    while True:
        response, status_code = get(
            service=f"policy/{policy_id}/accounts",
            params={
                "cursor": cursor,
            },
            api_key=api_key,
            preprod=preprod,
        )

        yield from response.get("data", [])

        cursor = response.get("next_cursor")

        if not cursor:
            break


def get_assets(policy_id: str, api_key: str = None, preprod: bool = False) -> Iterable[dict]:
    check_str(policy_id, "gomaestroorg.policy_id")
    policy_id = policy_id.strip().lower()

    cursor = None

    while True:
        response, status_code = get(
            service=f"policy/{policy_id}/assets",
            params={
                "cursor": cursor,
            },
            api_key=api_key,
            preprod=preprod,
        )

        for item in response.get("data", []):
            quantity = int(item["total_supply"])

            if quantity == 0:
                continue

            yield item

        cursor = response.get("next_cursor")

        if not cursor:
            break


def get_lock_slot(policy_id: str, api_key: str = None, preprod: bool = False) -> int:
    check_str(policy_id, "gomaestroorg.policy_id")

    response, status_code = get(
        service=f"policy/{policy_id}",
        api_key=api_key,
        preprod=preprod,
    )

    for script in response["data"]["script"]["json"]["scripts"]:
        if script["type"] == "before":
            return int(script["slot"])

    return None


def get_supply(policy_id: str, api_key: str = None, preprod: bool = False) -> int:
    check_str(policy_id, "gomaestroorg.policy_id")

    response, status_code = get(
        service=f"policy/{policy_id}",
        api_key=api_key,
        preprod=preprod,
    )

    total_supply = int(response["data"]["total_supply"])

    response, status_code = get(
        service=f"assets/{policy_id}",
        api_key=api_key,
        preprod=preprod,
    )

    try:
        royalty_token_supply = int(response["data"]["total_supply"])
    except KeyError:
        royalty_token_supply = 0

    return total_supply - royalty_token_supply
