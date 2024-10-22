import asyncio
import polars as pl

from hypermanager.events import EventConfig
from hypermanager.networks import HyperSyncClients
from hypermanager.schema import COMMON_TRANSACTION_MAPPING, COMMON_BLOCK_MAPPING
from hypermanager.manager import HyperManager
from hypersync import ColumnMapping


# optimism https://optimistic.etherscan.io/address/0xe8CDF27AcD73a434D661C84887215F7598e7d0d3
# https://github.com/stargate-protocol/stargate-v2/blob/main/packages/stg-evm-v2/deployments/optimism-mainnet/StargateMultiRewarder.json # chain deployment address
# https://github.com/stargate-protocol/stargate-v2/blob/main/packages/stg-evm-v2/src/StargateBase.sol # events
contract: str = "0xe8CDF27AcD73a434D661C84887215F7598e7d0d3".lower()
hypersync_client: str = HyperSyncClients.OPTIMISM.client

event_configs = [
    EventConfig(
        name="AddressConfigSet",
        signature=("AddressConfigSet(AddressConfig config)"),
        contract=contract,
        column_mapping=ColumnMapping(
            transaction=COMMON_TRANSACTION_MAPPING,
            block=COMMON_BLOCK_MAPPING,
        ),
    ),
    EventConfig(
        name="CreditsSent",
        signature=("CreditsSent(uint32 dstEid, Credit[] credits)"),
        contract=contract,
        column_mapping=ColumnMapping(
            transaction=COMMON_TRANSACTION_MAPPING,
            block=COMMON_BLOCK_MAPPING,
        ),
    ),
    EventConfig(
        name="CreditsReceived",
        signature=("CreditsReceived(uint32 srcEid, Credit[] credits)"),
        contract=contract,
        column_mapping=ColumnMapping(
            transaction=COMMON_TRANSACTION_MAPPING,
            block=COMMON_BLOCK_MAPPING,
        ),
    ),
    EventConfig(
        name="UnreceivedTokenCached",
        signature=("UnreceivedTokenCached()"),
        contract=contract,
        column_mapping=ColumnMapping(
            transaction=COMMON_TRANSACTION_MAPPING,
            block=COMMON_BLOCK_MAPPING,
        ),
    ),
    EventConfig(
        name="OFTPathSet",
        signature=("OFTPathSet(uint32 dstEid, bool oft)"),
        contract=contract,
        column_mapping=ColumnMapping(
            transaction=COMMON_TRANSACTION_MAPPING,
            block=COMMON_BLOCK_MAPPING,
        ),
    ),
    EventConfig(
        name="PauseSet",
        signature=("PauseSet(bool paused)"),
        contract=contract,
        column_mapping=ColumnMapping(
            transaction=COMMON_TRANSACTION_MAPPING,
            block=COMMON_BLOCK_MAPPING,
        ),
    ),
    EventConfig(
        name="PlannerFeeWithdrawn",
        signature=("PlannerFeeWithdrawn(uint256 amount)"),
        contract=contract,
        column_mapping=ColumnMapping(
            transaction=COMMON_TRANSACTION_MAPPING,
            block=COMMON_BLOCK_MAPPING,
        ),
    ),
    EventConfig(
        name="TreasuryFeeAdded",
        signature=("TreasuryFeeAdded(uint64 amountSD)"),
        contract=contract,
        column_mapping=ColumnMapping(
            transaction=COMMON_TRANSACTION_MAPPING,
            block=COMMON_BLOCK_MAPPING,
        ),
    ),
    EventConfig(
        name="TreasuryFeeWithdrawn",
        signature=("TreasuryFeeWithdrawn(address to, uint64 amountSD)"),
        contract=contract,
        column_mapping=ColumnMapping(
            transaction=COMMON_TRANSACTION_MAPPING,
            block=COMMON_BLOCK_MAPPING,
        ),
    ),
]


async def get_events():
    for event_config in event_configs:
        try:
            manager = HyperManager(url=hypersync_client)
            df: pl.DataFrame = await manager.execute_event_query(
                event_config, save_data=True, tx_data=True
            )

            # Check if the DataFrame is empty
            if df.is_empty():
                print(f"No events found for {event_config.name}, continuing...")
                continue

            # Process the non-empty DataFrame
            print(f"Events found for {event_config.name}:")
            print(df)

        except Exception as e:
            print(f"Error querying {event_config.name}: {e}")


if __name__ == "__main__":
    asyncio.run(get_events())
