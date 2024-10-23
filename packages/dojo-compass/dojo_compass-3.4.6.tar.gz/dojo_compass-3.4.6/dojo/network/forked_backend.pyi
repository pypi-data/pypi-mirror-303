from _typeshed import Incomplete
from datetime import datetime
from decimal import Decimal
from dojo.common.constants import Chain as Chain
from dojo.config import cfg as cfg
from dojo.network import block_date as block_date
from dojo.network._rpc_checks import RPCChecker as RPCChecker
from dojo.network.base_backend import BaseBackend as BaseBackend, patch_provider as patch_provider

anvil_autoImpersonateAccount: Incomplete
logger: Incomplete

def anvil_cmd(rpc_url: str, block_number: int, port: int) -> str: ...

class ForkedBackend(BaseBackend):
    def __init__(self, chain: Chain, port: int | None = None) -> None: ...
    start_block: Incomplete
    end_block: Incomplete
    web3: Incomplete
    block: Incomplete
    def connect(self, date_range: tuple[datetime, datetime], backend: str = 'anvil') -> None: ...
    def mint_token(self, token: str, quantity: int | Decimal) -> None: ...
