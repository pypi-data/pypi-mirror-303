from dataclasses import dataclass

from .gitstatus import GitStatus
from .jsondataclass import JSONDataClass


@dataclass
class TaskRecord(JSONDataClass):
    name: str
    pool: str
    points: int
    n_questions: int
    git_status: GitStatus
