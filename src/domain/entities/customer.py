
from uuid import UUID
from .base_entity import BaseEntity

class Customer(BaseEntity):
  id: UUID
  name: str
  email: str
  phone: str = ""
  address: str = ""
  
  def __init__(
    self, 
    id: UUID, 
    name: str, 
    email: str, 
    phone: str = "", 
    address: str = ""
  ):
    super().__init__(id)
    self.name = name
    self.email = email
    self.phone = phone
    self.address = address
    
  def validate(self):
    if not self.id or not isinstance(self.id, UUID): raise ValueError("id needs to be an uuid")
    if not self.name or not isinstance(self.name, str): raise ValueError("name needs to be a string")
    if not self.email or not isinstance(self.email, str): raise ValueError("email needs to be a string")
      