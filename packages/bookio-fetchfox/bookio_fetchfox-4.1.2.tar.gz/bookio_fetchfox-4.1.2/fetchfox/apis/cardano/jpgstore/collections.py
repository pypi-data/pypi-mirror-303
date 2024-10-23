from typing import Iterable

from fetchfox.checks import check_str
from .common import get


def get_sales(policy_id: str) -> Iterable[dict]:
    check_str(policy_id, "jpgstore.policy_id")
    policy_id = policy_id.strip().lower()

    txs = set()

    last_date = ""

    while True:
        response, status_code = get(
            service=f"collection/{policy_id}/v2/transactions",
            params={
                "lastDate": last_date,
                "count": 50,
            },
            headers={
                "x-jpgstore-csrf-protection": "1",
            },
        )

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
