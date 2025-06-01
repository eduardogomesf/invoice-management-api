from fastapi import FastAPI

def create_app(title = "unnamed-app"):
  app = FastAPI(title=title)

  return app
  