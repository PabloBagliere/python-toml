from condition.condition import Condition
from dataclasses import dataclass


@dataclass
class Field:
    name: str
    type: str
    primary: bool = False
    length: int = None
    alias: str = None
    condition: list[Condition] = None
    kwargs: dict = None

    def __init__(
        self,
        name: str,
        field_type: str,
        primary: bool = False,
        length: int = None,
        alias: str = None,
        condition: list[Condition] = None,
        **kwargs
    ):
        self.name = name
        self.type = field_type
        self.primary = primary
        self.length = length
        self.alias = alias
        self.condition = condition
        self.kwargs = kwargs
