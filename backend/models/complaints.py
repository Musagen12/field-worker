import uuid
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
import enum


class ComplaintCategory(str, enum.Enum):
    poor_quality = "poor_quality"
    delay = "delay"
    misconduct = "misconduct"
    other = "other"


class ComplaintStatus(str, enum.Enum):
    pending = "pending"       # Submitted, not reviewed yet
    reviewed = "reviewed"     # Admin has looked at it
    resolved = "resolved"     # Action taken / closed


class Complaint(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    description: str
    category: ComplaintCategory
    evidence: Optional[str] = None  # could be JSON list of URLs if you later allow uploads
    status: ComplaintStatus = Field(default=ComplaintStatus.pending)
    location: Optional[str] = None  # helps identify where issue happened
    submitted_at: datetime = Field(default_factory=datetime.now, nullable=False)  # ✅ fixed