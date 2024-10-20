from enum import Enum

class StrEnum(str, Enum): ...

class Chain(StrEnum):
    ETHEREUM = 'ethereum'
    ARBITRUM = 'arbitrum'
