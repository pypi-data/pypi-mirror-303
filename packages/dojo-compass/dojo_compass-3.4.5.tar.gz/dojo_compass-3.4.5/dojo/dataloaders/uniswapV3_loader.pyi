from _typeshed import Incomplete
from datetime import datetime
from dojo.common.constants import Chain as Chain
from dojo.config import cfg as cfg
from dojo.dataloaders.base_loader import BaseLoader as BaseLoader
from dojo.dataloaders.config import CONNECTION_POOL as CONNECTION_POOL
from dojo.dataloaders.exceptions import MissingIngestedData as MissingIngestedData
from dojo.dataloaders.formats import Event as Event, UniswapV3Burn as UniswapV3Burn, UniswapV3Collect as UniswapV3Collect, UniswapV3Initialize as UniswapV3Initialize, UniswapV3Mint as UniswapV3Mint, UniswapV3Swap as UniswapV3Swap
from dojo.network import block_date as block_date

memory: Incomplete

class UniswapV3Loader(BaseLoader):
    pools: Incomplete
    def __init__(self, rpc_url: str, chain: Chain, env_name: str, date_range: tuple[datetime, datetime], pools: list[str]) -> None: ...
