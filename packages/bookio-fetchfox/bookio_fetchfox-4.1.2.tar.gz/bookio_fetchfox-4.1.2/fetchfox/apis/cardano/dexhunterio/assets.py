from typing import Iterable, Optional

from fetchfox.checks import check_str
from .common import get, post


def get_orders(asset_id: str, partner_code: str = None) -> Iterable[dict]:
    check_str(asset_id, "dexhunterio.asset_id")

    body = {
        "filters": [
            {
                "filterType": "TOKENID",
                "values": [asset_id],
            },
            {
                "filterType": "STATUS",
                "values": ["COMPLETED"],
            },
        ],
        "orderSorts": "STARTTIME",
        "page": 0,
        "perPage": 100,
        "sortDirection": "DESC",
    }

    page = -1

    while True:
        page += 1
        body["page"] = page

        response = post(
            "swap/globalOrders",
            body=body,
            partner_code=partner_code,
        )

        if not response.get("orders"):
            break

        yield from response["orders"]


def get_average_price(asset_id: str, partner_code: str = None) -> Optional[float]:
    check_str(asset_id, "dexhunterio.asset_id")

    response = get(
        service=f"swap/averagePrice/{asset_id}/ADA",
        partner_code=partner_code,
    )

    if response is None:
        return None

    return response.get("price_ba")


def get_pair_stats(asset_id: str, partner_code: str = None) -> dict:
    check_str(asset_id, "dexhunterio.asset_id")

    return get(
        service=f"swap/pairStats/{asset_id}/ADA",
        partner_code=partner_code,
    )
