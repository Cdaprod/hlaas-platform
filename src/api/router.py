from fastapi import APIRouter
from ..services.data_service import get_items

item_router = APIRouter()

@item_router.get("/items")
async def read_items():
    return get_items()