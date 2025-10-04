import uuid
from datetime import datetime
from sqlmodel import SQLModel, Field, Column, Enum
import enum

class UserStatus(str, enum.Enum):
    active = "active"
    under_investigation = "under_investigation"\

class UserRole(str, enum.Enum):
    worker = "worker"
    admin = "admin"

# class User(SQLModel, table=True):
#     id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
#     username: str = Field(index=True, unique=True, nullable=False)
#     password_hash: str = Field(nullable=False)
#     role: UserRole = Field(default=UserRole.worker)
#     status: UserStatus = Field(default=UserStatus.active)
#     created_at: datetime = Field(default_factory=datetime.now)
#     updated_at: datetime = Field(default_factory=datetime.now)

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    username: str = Field(index=True, unique=True, nullable=False)
    password_hash: str = Field(nullable=False)
    phone_number: str = Field(index=True, unique=True, nullable=False)  # ✅ new field
    role: UserRole = Field(default=UserRole.worker, nullable=False)
    status: UserStatus = Field(default=UserStatus.active, nullable=False)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.now, nullable=False)