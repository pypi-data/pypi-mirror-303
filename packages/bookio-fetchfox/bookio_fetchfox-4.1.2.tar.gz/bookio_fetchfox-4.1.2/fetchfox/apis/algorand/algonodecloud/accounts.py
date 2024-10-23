from typing import Iterable

from fetchfox.checks import check_str
from .common import get


def get_assets(address: str, type: str = "assets") -> Iterable[dict]:
    check_str(address, "algonodecloud.address")
    address = address.strip().upper()

    next_token = None

    while True:
        response, status_code = get(
            service=f"accounts/{address}/{type}",
            params={
                "next": next_token,
            },
        )

        for asset in response["assets"]:
            yield asset

        next_token = response.get("next-token")

        if not next_token:
            break


def get_created_assets(address: str) -> Iterable[int]:
    for asset in get_assets(address, type="created-assets"):
        yield asset["index"]


def get_created_supply(address: str) -> int:
    return len(list(get_created_assets(address)))


def get_balance(address: str) -> Iterable[str]:
    check_str(address, "algonodecloud.address")
    address = address.strip().upper()

    response, status_code = get(
        service=f"accounts/{address}",
        params={
            "include-all": "false",
        },
    )

    return int(response["account"]["amount"]) / 10**6


def get_transactions(address: str) -> Iterable[dict]:
    check_str(address, "algonodecloud.address")
    address = address.strip().upper()

    next_token = None

    while True:
        response, status_code = get(
            service=f"accounts/{address}/transactions",
            params={
                "next": next_token,
            },
        )

        yield from response["transactions"]

        next_token = response.get("next-token")

        if not next_token:
            break
