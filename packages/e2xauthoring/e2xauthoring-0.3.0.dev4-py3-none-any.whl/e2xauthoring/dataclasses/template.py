from dataclasses import dataclass, field
from typing import List

from .jsondataclass import JSONDataClass


@dataclass
class TemplateRecord(JSONDataClass):
    name: str
    variables: List[str]


@dataclass
class TemplateCollectionRecord(JSONDataClass):
    templates: List[TemplateRecord] = field(default_factory=list)
