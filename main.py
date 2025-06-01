import os
import uvicorn
from src.create_app import create_app, load_routes
from src.api.rest import get_routers

if __name__ == "__main__":
  app = create_app("invoice-management-api")
  
  load_routes(app, get_routers())
      
  port = int(os.getenv("PORT", 8000))
  uvicorn.run(app, host="0.0.0.0", port=port)