from fastapi import FastAPI
from .api.v1_endpoints import router as v1_router
from .api.routers import item_router
from .core.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/")
async def root():
    return {"message": "Welcome to the HLaaS Platform API Gateway"}

# Include API routers
app.include_router(v1_router, prefix="/api/v1")
app.include_router(item_router)
# Additional routers can be included as needed