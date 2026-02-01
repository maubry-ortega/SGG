from fastapi import APIRouter
from src.modules.auth.router import router as auth_router
from src.modules.users.router import router as users_router
from src.modules.governance.router import router as governance_router
from src.modules.learning.router import router as learning_router

api_router = APIRouter()


# Module inclusions:
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(governance_router, prefix="/gov", tags=["Governance"])
api_router.include_router(learning_router, prefix="/learning", tags=["Saggi Grid"])



@api_router.get("/health-grid", tags=["Health"])
def health_grid():
    return {"status": "SGG Core Grid operational"}
