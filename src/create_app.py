from fastapi import FastAPI, APIRouter

def create_app(title = "unnamed-app"):
  app = FastAPI(title=title)

  return app
  
def load_routes(app: FastAPI, routers: list[APIRouter] = []):
    router = APIRouter(prefix="/api/v1")
  
    for r in routers:
      router.include_router(r)
      
    app.include_router(router)