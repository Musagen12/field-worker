# import uuid
# from datetime import datetime
# from typing import Optional
# from sqlmodel import SQLModel, Field, Relationship
# import enum

# class TaskStatus(str, enum.Enum):
#     pending = "pending"
#     in_progress = "in_progress"
#     completed = "completed"

# class Task(SQLModel, table=True):
#     id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True, index=True)
#     title: str
#     description: str
#     status: TaskStatus = Field(default=TaskStatus.pending)
#     assigned_to: str 
#     assigned_by: str
#     created_at: datetime = Field(default_factory=datetime.utcnow)
#     updated_at: datetime = Field(default_factory=datetime.utcnow)  

import uuid
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
import enum


class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class Task(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True, index=True)
    title: str
    description: str
    status: TaskStatus = Field(default=TaskStatus.pending)
    assigned_to: str
    assigned_by: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    evidences: list["TaskEvidence"] = Relationship(back_populates="task")


class TaskEvidence(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True, index=True)
    task_id: str = Field(foreign_key="task.id")
    file_url: str
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)

    task: Task = Relationship(back_populates="evidences")
