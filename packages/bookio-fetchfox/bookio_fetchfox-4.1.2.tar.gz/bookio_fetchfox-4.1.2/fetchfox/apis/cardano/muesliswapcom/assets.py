from cachetools.func import ttl_cache

from fetchfox.blockchains.cardano.utils import split_asset_id
from fetchfox.checks import check_str
from .common import get


@ttl_cache(ttl=60)
def get_price(asset_id: str) -> float:
    check_str(asset_id, "muesliswapcom.asset_id")

    policy_id, asset_name, _ = split_asset_id(asset_id)

    response, status_code = get(
        service="price",
        params={
            "quote-policy-id": policy_id,
            "quote-tokenname": asset_name,
        },
    )

    return response["price"]
