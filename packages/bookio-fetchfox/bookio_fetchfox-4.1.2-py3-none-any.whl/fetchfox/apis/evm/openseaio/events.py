import logging
from typing import Iterable

from fetchfox.checks import check_str
from . import collections
from .common import get

logger = logging.getLogger(__name__)


def get_sales(contract_address: str, blockchain: str, slug: str = None, api_key: str = None) -> Iterable[dict]:
    check_str(contract_address, "openseaio.contract_address")
    contract_address = contract_address.strip().lower()

    check_str(blockchain, "openseaio.blockchain")

    if not slug:
        slug = collections.get_slug(
            contract_address,
            blockchain,
            api_key=api_key,
        )

    cursor = ""

    while True:
        response, status_code = get(
            service=f"events/collection/{slug}",
            params={
                "event_type": "sale",
                "next": cursor,
            },
            api_key=api_key,
        )

        for event in response["asset_events"]:
            if event["event_type"] != "sale":
                continue

            yield event

        cursor = response.get("next")

        if not cursor:
            break
