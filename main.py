import os
import uvicorn
from fastapi import APIRouter
from src.create_app import create_app
from src.controllers.health import router as health_router

if __name__ == "__main__":
  app = create_app("invoice-management-api")
  
  router = APIRouter(prefix="/api/v1")
  router.include_router(health_router)
  
  app.include_router(router)
    
  port = int(os.getenv("PORT", 8000))
  uvicorn.run(app, host="0.0.0.0", port=port)