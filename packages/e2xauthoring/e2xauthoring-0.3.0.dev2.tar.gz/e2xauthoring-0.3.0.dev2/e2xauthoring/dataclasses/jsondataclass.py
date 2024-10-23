from dataclasses import asdict, dataclass


@dataclass
class JSONDataClass:
    def to_json(self):
        return asdict(self)
