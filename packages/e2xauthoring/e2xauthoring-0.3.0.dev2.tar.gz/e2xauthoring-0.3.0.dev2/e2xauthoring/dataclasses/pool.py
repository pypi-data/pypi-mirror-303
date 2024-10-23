from dataclasses import dataclass, field
from typing import List

from .jsondataclass import JSONDataClass
from .task import TaskRecord


@dataclass
class PoolRecord(JSONDataClass):
    name: str
    base_path: str
    n_tasks: int = 0
    tasks: List[TaskRecord] = field(default_factory=list)
    is_repo: bool = False


@dataclass
class PoolCollectionRecord(JSONDataClass):
    pools: List[PoolRecord] = field(default_factory=list)
