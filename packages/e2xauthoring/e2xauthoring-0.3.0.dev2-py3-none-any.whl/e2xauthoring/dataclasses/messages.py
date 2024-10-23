from dataclasses import dataclass
from typing import Any

from .jsondataclass import JSONDataClass


@dataclass
class SuccessMessage(JSONDataClass):
    success: bool = True
    message: str = ""
    data: Any = None


@dataclass
class ErrorMessage(JSONDataClass):
    success: bool = False
    error: str = ""
