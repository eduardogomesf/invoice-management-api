from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class CustomerDTO(BaseModel):
  id: UUID
  name: str
  email: str
  phone: Optional[str] = ""
  address: Optional[str] = ""
