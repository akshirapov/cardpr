from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {"status": "success", "data": None}
