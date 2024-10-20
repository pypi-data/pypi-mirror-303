import abc
from _typeshed import Incomplete
from abc import ABC
from datetime import datetime
from dojo.common.constants import Chain as Chain
from dojo.config import cfg as cfg
from dojo.dataloaders.formats import Event as Event, UniswapV3Burn as UniswapV3Burn, UniswapV3Collect as UniswapV3Collect, UniswapV3Initialize as UniswapV3Initialize, UniswapV3Mint as UniswapV3Mint, UniswapV3Swap as UniswapV3Swap
from typing import Any

QUERY_FOR_DATA_INGESTED_BY_DOJO: Incomplete

def address_to_name(chain: Chain, protocol: str, address: str) -> str: ...

class BaseLoader(ABC, metaclass=abc.ABCMeta):
    env_name: Incomplete
    date_range: Incomplete
    rpc_url: Incomplete
    chain: Incomplete
    def __init__(self, rpc_url: str, chain: Chain, env_name: str, date_range: tuple[datetime, datetime], **kwargs: Any) -> None: ...
