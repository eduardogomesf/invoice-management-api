from ..use_cases.create_customer import CreateCustomerUseCase

def get_create_customer_use_case() -> CreateCustomerUseCase:
  return CreateCustomerUseCase()