from .common import get


def get_transaction(tx_hash: str, api_key: str = None, preprod: bool = False) -> dict:
    response, status_code = get(
        service=f"transactions/{tx_hash}",
        api_key=api_key,
        preprod=preprod,
    )

    return response["data"]
