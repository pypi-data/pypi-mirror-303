from enum import Enum


class AppVersion(str, Enum):
    VALUE_0 = "2024.1.0"
    VALUE_1 = "2024.2.0"
    VALUE_2 = "2024.2.1"

    def __str__(self) -> str:
        return str(self.value)
