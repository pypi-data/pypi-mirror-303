from _typeshed import Incomplete
from datetime import datetime
from decimal import Decimal
from dojo import money as money
from dojo.common.constants import Chain as Chain
from dojo.network.base_backend import BaseBackend as BaseBackend, patch_provider as patch_provider

anvil_autoImpersonateAccount: Incomplete
logger: Incomplete

def anvil_cmd(port: int) -> str: ...

class LocalBackend(BaseBackend):
    def __init__(self, *, chain: Chain, port: int | None = None) -> None: ...
    start_block: Incomplete
    end_block: Incomplete
    web3: Incomplete
    block: Incomplete
    def connect(self, date_range: tuple[datetime, datetime], backend: str = 'anvil') -> None: ...
    def mint_token(self, token: str, quantity: int | Decimal) -> None: ...
