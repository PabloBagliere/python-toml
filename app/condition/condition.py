from dataclasses import dataclass


@dataclass
class Condition:
    operator: str
    value: str
    condition: str = "AND"

    def __init__(self, operator: str = None, value: str = None, condition: str = "AND"):
        self.operator = operator
        self.value = value
        self.condition = condition
