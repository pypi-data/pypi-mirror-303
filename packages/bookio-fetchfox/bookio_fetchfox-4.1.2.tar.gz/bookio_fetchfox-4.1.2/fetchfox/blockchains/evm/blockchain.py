import logging
from datetime import datetime
from idlelib.pyparse import trans
from typing import Iterable, List, Optional, Tuple

import pytz
from cachetools.func import ttl_cache

from fetchfox.apis import bookio
from fetchfox.apis.evm import moralisio, ensideascom, openseaio
from fetchfox.blockchains.base import Blockchain
from fetchfox.constants.blockchains import ETHEREUM
from fetchfox.constants.marketplaces import OPENSEA_IO
from fetchfox.dtos import (
    AssetDTO,
    CampaignDTO,
    CampaignPricingDTO,
    FloorDTO,
    HoldingDTO,
    ListingDTO,
    SaleDTO,
    TransactionDTO,
    TransactionInputOutputDTO,
    TransactionAssetDTO,
)
from fetchfox.helpers import formatters
from . import utils
from .exceptions import (
    InvalidEvmAssetIdException,
    InvalidEvmCollectionIdException,
    InvalidEvmAccountException,
)

logger = logging.getLogger(__name__)


class Evm(Blockchain):
    def __init__(
        self,
        name: str,
        currency: str,
        logo: str,
        moralisio_api_key: str = None,
        openseaio_api_key: str = None,
        preprod: bool = False,
    ):
        super().__init__(name, currency, logo, preprod=preprod)

        self.moralisio_api_key: str = moralisio_api_key
        self.openseaio_api_key: str = openseaio_api_key

    # checks
    def check_account(self, account: str, exception: bool = True) -> bool:
        valid = utils.is_account(account)

        if not valid and exception:
            raise InvalidEvmAccountException(account, self.name)

        return valid

    def check_asset_id(self, asset_id: str, exception: bool = True) -> bool:
        valid = utils.is_asset_id(asset_id)

        if not valid and exception:
            raise InvalidEvmAssetIdException(asset_id, self.name)

        return valid

    def check_collection_id(self, collection_id: str, exception: bool = True) -> bool:
        valid = utils.is_address(collection_id)

        if not valid and exception:
            raise InvalidEvmCollectionIdException(collection_id, self.name)

        return valid

    # accounts
    @ttl_cache(ttl=600)
    def get_account_main_address(self, account: str, exception: bool = False) -> Optional[str]:
        if not self.check_account(account, exception=exception):
            return None

        resolved = self.resolve_account_name(account)

        return resolved or account

    def get_account_name(self, account: str) -> str:
        if utils.is_ens_domain(account):
            return account

        if utils.is_address(account):
            return ensideascom.get_ens_domain(account)

        return None

    def resolve_account_name(self, name: str) -> str:
        if utils.is_ens_domain(name):
            return ensideascom.resolve_ens_domain(name)

        return None

    # account attributes
    def get_account_assets(self, account: str, collection_id: str = None) -> Iterable[HoldingDTO]:
        address = self.get_account_main_address(account, exception=True)

        account_assets = moralisio.get_address_assets(
            address,
            blockchain=self.name,
            api_key=self.moralisio_api_key,
            preprod=self.preprod,
        )

        for asset in account_assets:
            yield HoldingDTO(
                collection_id=asset["token_address"],
                asset_id=asset["token_id"],
                address=address,
                amount=float(asset["amount"]),
            )

    def get_account_balance(self, account: str) -> Tuple[float, str]:
        address = self.get_account_main_address(account, exception=True)

        balance = moralisio.get_address_balance(
            address,
            blockchain=self.name,
            api_key=self.moralisio_api_key,
            preprod=self.preprod,
        )

        return balance, self.currency

    def get_account_transactions(self, account: str, last: int = 10) -> Iterable[TransactionDTO]:
        def parse_input_output(type: str, transfers: List[dict]):
            for transfer in transfers:
                if type == "erc20":
                    decimals = int(transfer.get("token_decimals", "0"))
                    amount = float(transfer["value"]) / 10**decimals
                    unit = transfer["token_symbol"]
                elif type == "nft":
                    amount = float(transfer["amount"])
                    unit = transfer["token_address"] + "/" + transfer["token_id"]
                else:
                    decimals = 18
                    amount = float(transfer["value"]) / 10**decimals
                    unit = transfer["token_symbol"]

                tx_input = TransactionInputOutputDTO(
                    address=transfer["from_address"],
                    assets=[
                        TransactionAssetDTO(
                            amount=amount,
                            unit=unit,
                        ),
                    ],
                )

                tx_output = TransactionInputOutputDTO(
                    address=transfer["to_address"],
                    assets=[
                        TransactionAssetDTO(
                            amount=amount,
                            unit=unit,
                        ),
                    ],
                )

                yield tx_input, tx_output

        address = self.get_account_main_address(account, exception=True)

        account_transactions = moralisio.get_wallet_transactions(
            address,
            blockchain=self.name,
            api_key=self.moralisio_api_key,
            preprod=self.preprod,
        )

        for index, transaction in enumerate(account_transactions):
            if index >= last:
                break

            message = transaction.get("summary")

            inputs, outputs = [], []

            for type in ["native", "nft", "erc20"]:
                transfers = transaction.get(f"{type}_transfers")

                for tx_input, tx_output in parse_input_output(type, transfers):
                    inputs.append(tx_input)
                    outputs.append(tx_output)

            yield TransactionDTO(
                blockchain=self.name,
                address=address,
                tx_hash=transaction["hash"],
                message=message,
                inputs=inputs,
                outputs=outputs,
            )

    # assets
    def get_asset(self, collection_id: str, asset_id: str, *args, **kwargs) -> AssetDTO:
        self.check_collection_id(collection_id)
        self.check_asset_id(asset_id)

        asset_data = moralisio.get_asset_data(
            contract_address=collection_id,
            asset_id=asset_id,
            blockchain=self.name,
            api_key=self.moralisio_api_key,
            preprod=self.preprod,
        )

        return AssetDTO(
            collection_id=collection_id,
            asset_id=asset_id,
            metadata=asset_data["metadata"],
        )

    def get_asset_holders(self, collection_id: str, asset_id: str, *args, **kwargs) -> Iterable[HoldingDTO]:
        self.check_collection_id(collection_id)
        self.check_asset_id(asset_id)

        holders = moralisio.get_asset_holders(
            collection_id,
            asset_id=asset_id,
            blockchain=self.name,
            api_key=self.moralisio_api_key,
            preprod=self.preprod,
        )

        for holder in holders:
            yield HoldingDTO(
                collection_id=holder["contract_address"],
                asset_id=holder["asset_id"],
                address=holder["address"],
                amount=float(holder["amount"]),
            )

    # collections
    def get_collection_assets(self, collection_id: str, fetch_metadata: bool = True, *args, **kwargs) -> Iterable[AssetDTO]:
        self.check_collection_id(collection_id)

        if fetch_metadata:
            asset_id = -1

            while True:
                try:
                    asset_id += 1

                    yield self.get_asset(
                        collection_id=collection_id,
                        asset_id=str(asset_id),
                    )
                except ValueError:
                    raise
                except Exception as exc:
                    break
        else:
            collection_assets = moralisio.get_contract_assets(
                contract_address=collection_id,
                blockchain=self.name,
                api_key=self.moralisio_api_key,
                preprod=self.preprod,
            )

            for asset_id in collection_assets:
                yield AssetDTO(
                    collection_id=collection_id,
                    asset_id=asset_id,
                    metadata={},
                )

    def get_collection_floor(self, collection_id: str, *args, **kwargs) -> FloorDTO:
        self.check_collection_id(collection_id)

        floor = None
        count = 0

        for listing in self.get_collection_listings(collection_id):
            count += 1

            if floor is None:
                floor = listing
            elif listing.usd < floor.usd:
                floor = listing

        return FloorDTO(
            listing=floor,
            listing_count=count,
        )

    def get_collection_listings(self, collection_id: str, slug: str = None, *args, **kwargs) -> Iterable[ListingDTO]:
        self.check_collection_id(collection_id)

        collection_listings = openseaio.get_collection_listings(
            collection_id,
            blockchain=self.name,
            api_key=self.openseaio_api_key,
            slug=slug,
        )

        for listing in collection_listings:
            protocol_data = listing["protocol_data"]
            parameters = protocol_data["parameters"]

            price = listing["price"]["current"]

            asset_ids = []
            asset_names = []

            for offer in parameters["offer"]:
                if offer["token"].lower() != collection_id.lower():
                    continue

                asset_ids.append(offer["identifierOrCriteria"])
                asset_names.append("")

            if listing.get("eventTimestamp"):
                listed_at = datetime.utcfromtimestamp(parameters["startTime"])
            else:
                listed_at = datetime.now(tz=pytz.utc)

            marketplace_url = self.marketplace_url(
                collection_id=collection_id,
                asset_id=asset_ids[0],
            )

            yield ListingDTO(
                identifier=listing["order_hash"],
                collection_id=collection_id,
                asset_ids=asset_ids,
                asset_names=asset_names,
                listing_id=listing["order_hash"],
                marketplace=OPENSEA_IO,
                price=float(int(price["value"]) / 10 ** price["decimals"]),
                currency=price["currency"].replace("WETH", "ETH"),
                listed_at=listed_at,
                listed_by=parameters["offerer"],
                tx_hash=listing["order_hash"],
                marketplace_url=marketplace_url,
            )

    def get_collection_sales(self, collection_id: str, slug: str = None, *args, **kwargs) -> Iterable[SaleDTO]:
        self.check_collection_id(collection_id)

        collection_sale = openseaio.get_collection_sales(
            collection_id,
            blockchain=self.name,
            api_key=self.openseaio_api_key,
            slug=slug,
        )

        for sale in collection_sale:
            tx_hash = sale["transaction"]

            asset = sale["nft"]
            asset_id = asset["identifier"]
            asset_name = asset["name"]

            if sale.get("closing_date"):
                confirmed_at = datetime.fromtimestamp(
                    sale["closing_date"],
                    tz=pytz.utc,
                )
            else:
                confirmed_at = datetime.now(
                    tz=pytz.utc,
                )

            marketplace_url = self.marketplace_url(
                collection_id=collection_id,
                asset_id=asset_id,
            )

            explorer_url = self.explorer_url(
                tx_hash=tx_hash,
            )

            yield SaleDTO(
                identifier=f"{tx_hash}/{asset_id}",
                collection_id=collection_id,
                asset_ids=[asset_id],
                asset_names=[asset_name],
                tx_hash=tx_hash,
                marketplace=OPENSEA_IO,
                price=float(int(sale["payment"]["quantity"]) / 10 ** sale["payment"]["decimals"]),
                currency=sale["payment"]["symbol"].replace("WETH", "ETH"),
                confirmed_at=confirmed_at,
                sold_by=sale["seller"],
                bought_by=sale["buyer"],
                sale_id=sale["transaction"],
                marketplace_url=marketplace_url,
                explorer_url=explorer_url,
            )

    def get_collection_supply(self, collection_id: str, *args, **kwargs) -> int:
        self.check_collection_id(collection_id)

        return moralisio.get_contract_supply(
            collection_id,
            blockchain=self.name,
            api_key=self.moralisio_api_key,
            preprod=self.preprod,
        )

    def get_collection_holders(self, collection_id: str, *args, **kwargs) -> Iterable[HoldingDTO]:
        self.check_collection_id(collection_id)

        collection_owners = moralisio.get_contract_holders(
            collection_id,
            blockchain=self.name,
            api_key=self.moralisio_api_key,
            preprod=self.preprod,
        )

        for asset in collection_owners:
            yield HoldingDTO(
                collection_id=asset["contract_address"],
                asset_id=asset["asset_id"],
                address=asset["address"],
                amount=float(asset["amount"]),
            )

    # campaigns
    def get_campaigns(self, starts_after: datetime = None) -> Iterable[CampaignDTO]:
        def parse_pricing(pricing: dict) -> List[CampaignPricingDTO]:
            result = []

            if pricing.get("native_price"):
                result.append(
                    CampaignPricingDTO(
                        currency=self.currency,
                        amount=pricing["native_price"] / 10**18,
                    )
                )

            return result

        for campaign in bookio.get_campaigns():
            if not campaign.get("collection_id"):
                continue

            if campaign["blockchain"] != "evm":
                continue

            network = "mainnet" if self.name == ETHEREUM else self.name

            if campaign["network"] != network:
                continue

            collection_id = campaign["collection_id"]
            start_at = formatters.timestamp(campaign["start_at"])

            if starts_after is not None:
                if start_at < starts_after:
                    continue

            yield CampaignDTO(
                blockchain=self.name,
                parlamint_id=campaign["campaign_id"],
                collection_id=collection_id,
                name=campaign["name"],
                start_at=start_at,
                supply=campaign["total_deas"],
                limit=campaign["max_quantity"],
                mint_pricing=parse_pricing(
                    pricing=campaign.get("mint_price", {}),
                ),
                discount_pricing=parse_pricing(
                    pricing=campaign.get("discount_price", {}),
                ),
                bookstore_url=campaign["bookstore_url"],
                cover_url=campaign["cover_url"],
                explorer_url=self.explorer_url(
                    collection_id=collection_id,
                ),
            )

    # others
    def verify_otp(self, account: str, otp: float) -> TransactionDTO:
        return super().verify_otp(account.lower(), otp)

    # tokens
    def get_token_exchange(self, collection_id: str, asset_id: str) -> Optional[float]:
        self.check_collection_id(collection_id)
        self.check_asset_id(asset_id)

        return moralisio.get_token_price(
            collection_id,
            blockchain=self.name,
            api_key=self.moralisio_api_key,
            preprod=self.preprod,
        )

    # sanity
    def api_keys(self) -> List[str]:
        return [
            "m:{moralisio}".format(
                moralisio=self.moralisio_api_key[-3:] if self.moralisio_api_key else "none",
            ),
            "os:{openseaio}".format(
                openseaio=self.openseaio_api_key[-3:] if self.openseaio_api_key else "none",
            ),
        ]
