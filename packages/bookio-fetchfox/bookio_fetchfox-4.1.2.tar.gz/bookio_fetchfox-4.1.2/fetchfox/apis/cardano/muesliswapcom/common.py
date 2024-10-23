import os
from typing import Tuple

from fetchfox import rest

BASE_URL_DEFAULT = "https://api.muesliswap.com"
BASE_URL = os.getenv("MUESLISWAPCOM_BASE_URL") or BASE_URL_DEFAULT


def get(service: str, params: dict = None) -> Tuple[dict, int]:
    return rest.get(
        url=f"{BASE_URL}/{service}",
        params=params,
        sleep=0.5,
    )
