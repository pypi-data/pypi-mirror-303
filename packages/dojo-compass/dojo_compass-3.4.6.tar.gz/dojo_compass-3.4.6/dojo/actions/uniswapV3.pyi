from dataclasses import dataclass
from decimal import Decimal
from dojo.actions.base_action import BaseAction as BaseAction
from dojo.agents.base_agent import BaseAgent as BaseAgent
from dojo.network.constants import ZERO_ADDRESS as ZERO_ADDRESS
from dojo.observations import UniswapV3Observation as UniswapV3Observation

@dataclass
class UniswapV3Action(BaseAction[UniswapV3Observation]):
    def __init__(self, *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3Trade(UniswapV3Action):
    pool: str
    quantities: tuple[Decimal, Decimal]
    price_limit: Decimal | None = ...
    def __init__(self, pool, quantities, price_limit=..., *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3TradeToTickRange(UniswapV3Action):
    pool: str
    quantities: tuple[Decimal, Decimal]
    tick_range: tuple[int, int]
    def __init__(self, pool, quantities, tick_range, *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3Quote(UniswapV3Action):
    pool: str
    quantities: tuple[Decimal, Decimal]
    tick_range: tuple[int, int]
    liquidity: int = ...
    owner: str = ...
    def __init__(self, pool, quantities, tick_range, liquidity=..., owner=..., *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3ProvideLiquidity(UniswapV3Action):
    pool: str
    tick_range: tuple[int, int]
    liquidity: int
    def __init__(self, pool, tick_range, liquidity, *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3ProvideQuantities(UniswapV3Action):
    pool: str
    tick_range: tuple[int, int]
    amount0: Decimal
    amount1: Decimal
    owner: str = ...
    auto_trade: bool = ...
    def __init__(self, pool, tick_range, amount0, amount1, owner=..., auto_trade=..., *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3IncreaseLiquidity(UniswapV3Action):
    pool: str
    position_id: int
    liquidity: int
    owner: str = ...
    def __init__(self, pool, position_id, liquidity, owner=..., *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3WithdrawLiquidity(UniswapV3Action):
    position_id: int
    liquidity: int
    owner: str = ...
    def __init__(self, position_id, liquidity, owner=..., *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3LiquidatePosition(UniswapV3Action):
    position_id: int
    def __init__(self, position_id, *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3Collect(UniswapV3Action):
    pool: str
    quantities: tuple[Decimal, Decimal]
    tick_range: tuple[int, int]
    def __init__(self, pool, quantities, tick_range, *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3SetFeeProtocol(UniswapV3Action):
    pool: str
    quantities: tuple[Decimal, Decimal]
    __annotations__ = ...
    def __init__(self, pool, quantities, *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3CollectFull(UniswapV3Action):
    pool: str
    position_id: str
    def __init__(self, pool, position_id, *, agent, gas=..., gas_price=...) -> None: ...

@dataclass
class UniswapV3BurnNew(UniswapV3Action):
    position_id: str
    def __init__(self, position_id, *, agent, gas=..., gas_price=...) -> None: ...
