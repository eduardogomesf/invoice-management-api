from fastapi import APIRouter, Depends
from ...dto.customer import CustomerDTO
from ..dependencies import get_create_customer_use_case
from ...use_cases.create_customer import CreateCustomerUseCase

router = APIRouter(prefix="/customers")

@router.post("/")
def create_customer(
  customer_data: CustomerDTO, 
  create_customer_use_case: CreateCustomerUseCase = Depends(get_create_customer_use_case)
):
  id = create_customer_use_case.execute(customer_data)
  
  return id
