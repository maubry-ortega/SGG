from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.core.config import settings
from src.core.database import init_beanie_db
from src.api.v1.router import api_router
import logging

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create SQL Tables (Neon)
    from src.shared.models.user import Base
    from src.core.database import engine
    Base.metadata.create_all(bind=engine)
    
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

    # Global Exception Handler to ensure CORS headers are applied to 500s
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logging.error(f"Global error: {exc}", exc_info=True)
        response = JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error", "error": str(exc)},
        )
        origin = request.headers.get("origin")
        if origin:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Credentials"] = "true"
        return response

    # Set all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://localhost:5174",
            "http://127.0.0.1:5174",
            "http://localhost:5175",
        ],  
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API Routers
    app.include_router(api_router, prefix=settings.API_V1_STR)

    # Static Files for Uploads
    app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

    @app.get("/", tags=["Health"])
    def root():
        return {
            "message": f"Welcome to {settings.PROJECT_NAME} (Saggi) Core Engine",
            "status": "Running",
            "docs": "/docs"
        }

    return app

app = create_app()
