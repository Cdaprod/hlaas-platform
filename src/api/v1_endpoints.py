from fastapi import APIRouter
from ..services.example_service import perform_service

router = APIRouter()

@router.get("/example")
async def example_endpoint():
    # Call a service function
    result = perform_service()
    return {"message": result}