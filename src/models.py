from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Task:
    id: int
    description: str
    completed: bool = field(default=False)

    def to_dict(self):
        return {"id": self.id, "description": self.description, "completed": self.completed}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(id=data["id"], description=data["description"], completed=data.get("completed", False))
