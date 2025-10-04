import uuid
from datetime import datetime
from sqlmodel import SQLModel, Field
import enum

# Status for employee complaints
class EmployeeComplaintStatus(str, enum.Enum):
    pending = "pending"
    reviewed = "reviewed"
    resolved = "resolved"

class EmployeeComplaint(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    worker_id: uuid.UUID = Field(foreign_key="user.id", nullable=False)  # worker who submitted the complaint
    description: str
    status: EmployeeComplaintStatus = Field(default=EmployeeComplaintStatus.pending)
    submitted_at: datetime = Field(default_factory=datetime.utcnow)
