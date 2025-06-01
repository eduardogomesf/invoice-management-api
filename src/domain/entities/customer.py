
import uuid


class Customer:
  id: uuid.UUID
  name: str
  email: str
  phone: str = ""
  address: str = ""
  
  @staticmethod
  def create(name: str, email: str, phone: str = "", address: str = ""):
    return Customer(
      id=uuid.UUID(),
      name=name,
      email=email,
      phone=phone,
      address=address
    )