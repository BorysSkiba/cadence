from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/health", status_code=200)
def health():
    return {"service": "cadence", "status": "ok"}