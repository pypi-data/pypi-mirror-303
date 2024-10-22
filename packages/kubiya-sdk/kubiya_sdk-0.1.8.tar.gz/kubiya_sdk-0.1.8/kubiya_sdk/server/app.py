from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routes import discover, run, describe, visualize
import logging

logger = logging.getLogger(__name__)

def create_app():
    app = FastAPI(
        title="Kubiya SDK API Server",
        description="API for running workflows and tools using Kubiya SDK",
        version="1.0.0",
        docs_url="/docs",  # Swagger UI documentation
        redoc_url="/redoc"  # ReDoc documentation
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(discover.router)
    app.include_router(run.router)
    app.include_router(describe.router)
    app.include_router(visualize.router)

    @app.exception_handler(Exception)
    async def global_exception_handler(request, exc):
        logger.exception(f"Unhandled exception occurred: {str(exc)}")
        return {"detail": str(exc)}, 500

    return app
