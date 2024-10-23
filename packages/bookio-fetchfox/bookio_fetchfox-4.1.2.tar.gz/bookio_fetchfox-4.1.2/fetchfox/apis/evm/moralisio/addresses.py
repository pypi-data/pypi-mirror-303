from typing import Iterable

from fetchfox.checks import check_str
from .common import get


def get_balance(address: str, blockchain: str, api_key: str = None, preprod: bool = False) -> Iterable[dict]:
    check_str(address, "moralisio.address")
    address = address.strip().lower()

    response, status_code = get(
        service=f"{address}/balance",
        blockchain=blockchain,
        api_key=api_key,
        preprod=preprod,
    )

    return int(response["balance"]) / 10**18


def get_assets(address: str, blockchain: str, api_key: str = None, preprod: bool = False) -> Iterable[dict]:
    check_str(address, "moralisio.address")
    address = address.strip().lower()

    cursor = ""

    while True:
        response, status_code = get(
            service=f"{address}/nft",
            params={
                "cursor": cursor,
            },
            blockchain=blockchain,
            api_key=api_key,
            preprod=preprod,
        )

        yield from response.get("result", [])

        if not response.get("cursor"):
            break

        cursor = response["cursor"]
