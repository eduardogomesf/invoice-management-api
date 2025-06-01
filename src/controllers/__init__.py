from .health import router as health_router

def get_routers():
  return [health_router]