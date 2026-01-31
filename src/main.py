from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import settings
from src.core.database import init_beanie_db
from src.api.v1.router import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize Beanie (MongoDB)
    await init_beanie_db()
    yield

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=f"Welcome to {settings.PRODUCT_NAME} - One Brain, Two Faces.",
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        lifespan=lifespan
    )


    # Set all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API Routers
    app.include_router(api_router, prefix=settings.API_V1_STR)

    @app.get("/", tags=["Health"])
    def root():
        return {
            "message": f"Welcome to {settings.PROJECT_NAME} (Saggi) Core Engine",
            "status": "Running",
            "docs": "/docs"
        }

    return app

app = create_app()
