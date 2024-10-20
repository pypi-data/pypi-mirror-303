from decimal import Decimal
from dojo.agents.base_agent import BaseAgent as BaseAgent
from dojo.observations import BaseObservation as BaseObservation

class DummyAgent(BaseAgent):
    def __init__(self, initial_portfolio: dict[str, Decimal] | None = None, name: str = 'DummyAgent') -> None: ...
    def reward(self, obs: BaseObservation) -> float: ...
