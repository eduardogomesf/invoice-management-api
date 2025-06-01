from .health import router as health_router
from .customer import router as customer_router

def get_routers():
  return [health_router, customer_router]