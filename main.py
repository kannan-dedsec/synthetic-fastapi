"""
main.py

FastAPI application entrypoint with lifespan management, routers inclusion,
CORS middleware setup, and a health root endpoint.
"""

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, APIRouter, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Initialize logger
logger = logging.getLogger("uvicorn.error")


@asynccontextmanager
async def app_lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Lifespan context manager for startup and shutdown events.
    """
    logger.info("Starting up FastAPI application...")
    # Startup logic here (e.g., connect to DB, initialize cache, etc.)
    yield
    # Shutdown logic here (e.g., disconnect DB, cleanup resources)
    logger.info("Shutting down FastAPI application...")


def create_api_router() -> APIRouter:
    """
    Creates and returns the main API router with example endpoints.
    """
    router = APIRouter()

    @router.get("/ping", response_class=JSONResponse, tags=["Health"])
    async def ping() -> dict[str, str]:
        """
        Simple ping endpoint for health checking.
        """
        return {"message": "pong"}

    return router


def create_app() -> FastAPI:
    """
    Creates and configures the FastAPI application instance.
    """
    app = FastAPI(
        title="FastAPI Example Application",
        description="An example FastAPI project with lifespan, routers, CORS, and health endpoint.",
        version="1.0.0",
        lifespan=app_lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    origins = [
        "http://localhost",
        "http://localhost:3000",
        "https://myfrontend.com"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Root health endpoint
    @app.get("/", response_class=JSONResponse, status_code=status.HTTP_200_OK, tags=["Health"])
    async def root_health(request: Request) -> dict[str, str]:
        """
        Root health endpoint to verify server status.
        """
        client_host = request.client.host if request.client else "unknown"
        return {"status": "ok", "client": client_host}

    # Include routers
    api_router = create_api_router()
    app.include_router(api_router, prefix="/api")

    return app


app = create_app()