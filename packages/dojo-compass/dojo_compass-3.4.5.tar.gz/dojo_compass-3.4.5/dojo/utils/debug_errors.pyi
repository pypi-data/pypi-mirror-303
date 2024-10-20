from _typeshed import Incomplete
from dojo.config import cfg as cfg

gmx_abis: Incomplete
aave_abis: Incomplete

def debug_gmx_error(error_code: str) -> tuple[str, str]: ...
def debug_aave_error(error_code: str) -> str: ...
