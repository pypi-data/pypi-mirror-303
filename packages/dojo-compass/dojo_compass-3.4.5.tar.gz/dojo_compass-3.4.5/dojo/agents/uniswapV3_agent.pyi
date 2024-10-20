import abc
from dojo.agents.base_agent import BaseAgent as BaseAgent

class UniswapV3Agent(BaseAgent, metaclass=abc.ABCMeta):
    def get_liquidity_ownership_tokens(self) -> list[int]: ...
