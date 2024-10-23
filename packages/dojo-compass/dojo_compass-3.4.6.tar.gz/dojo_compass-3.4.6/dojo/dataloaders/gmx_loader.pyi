from _typeshed import Incomplete
from datetime import datetime
from dojo.common.constants import Chain as Chain
from dojo.dataloaders.base_loader import BaseLoader as BaseLoader
from dojo.dataloaders.config import CONNECTION_POOL as CONNECTION_POOL
from dojo.dataloaders.exceptions import MissingIngestedData as MissingIngestedData
from dojo.dataloaders.formats import GMXEvent as GMXEvent
from dojo.network import block_date as block_date

logger: Incomplete
GMX_EVENT_EMITTER_CONTRACT_ADDRESS: Incomplete

class GMXLoader(BaseLoader):
    def __init__(self, rpc_url: str, chain: Chain, env_name: str, date_range: tuple[datetime, datetime]) -> None: ...
