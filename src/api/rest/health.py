from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
  return "I am healthy"