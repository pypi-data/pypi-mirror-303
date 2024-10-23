from typing import Iterable

from fetchfox.checks import check_str
from .common import get


def get_listings(policy_id: str) -> Iterable[dict]:
    check_str(policy_id, "jpgstore.policy_id")
    policy_id = policy_id.strip().lower()

    cursor = ""

    while True:
        params = {}

        if cursor:
            params["cursor"] = cursor

        response, status_code = get(
            service=f"policy/{policy_id}/listings",
            params=params,
        )

        cursor = response.get("nextPageCursor")

        if not cursor:  # pragma: no cover
            break

        yield from response["listings"]

        transactions = response.get("transactions")

        if not transactions:  # pragma: no cover
            break

        for sale in transactions:
            tx_hash = sale["tx_hash"]

            if tx_hash in txs:
                continue

            txs.add(tx_hash)
            last_date = sale["created_at"]

            yield sale
