import asyncio
import polars as pl

from hypermanager.manager import HyperManager

hypersync_client: str = "https://mev-commit.hypersync.xyz"


async def get_events():
    manager: HyperManager = HyperManager(url=hypersync_client)

    await manager.get_txs(from_block=0, to_block=20_000_000, save_data=True)

    print("done")


if __name__ == "__main__":
    asyncio.run(get_events())
