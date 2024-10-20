from _typeshed import Incomplete
from datetime import datetime
from dojo.common.constants import Chain as Chain
from dojo.config import cfg as cfg
from dojo.dataloaders.base_loader import BaseLoader as BaseLoader
from dojo.dataloaders.config import CONNECTION_POOL as CONNECTION_POOL
from dojo.network import block_date as block_date

class AaveV3Loader(BaseLoader):
    file_paths: Incomplete
    def __init__(self, rpc_url: str, chain: Chain, env_name: str, date_range: tuple[datetime, datetime]) -> None: ...
