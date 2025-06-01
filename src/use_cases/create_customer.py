from ..dto.customer import CustomerDTO
from ..domain.entities.customer import Customer

class CreateCustomerUseCase:
  
  def execute(self, data: CustomerDTO):
    customer = Customer(
      id=data.id,
      name=data.name,
      email=data.email,
      phone=data.phone,
      address=data.address
    )
    return customer.id