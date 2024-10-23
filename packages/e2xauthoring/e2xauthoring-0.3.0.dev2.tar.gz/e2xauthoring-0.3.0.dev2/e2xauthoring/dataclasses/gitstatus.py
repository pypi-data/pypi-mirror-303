from dataclasses import dataclass, field
from typing import List, Optional

from .jsondataclass import JSONDataClass


@dataclass
class GitStatus(JSONDataClass):
    untracked: Optional[List[str]] = field(default_factory=list)
    unstaged: Optional[List[str]] = field(default_factory=list)
    staged: Optional[List[str]] = field(default_factory=list)
    status: Optional[str] = None
