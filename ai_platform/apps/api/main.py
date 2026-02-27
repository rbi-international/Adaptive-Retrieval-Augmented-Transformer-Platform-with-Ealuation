from contextlib import asynccontextmanager
from fastapi import FastAPI

from packages.core.logger import configure_logging, get_logger
from packages.core.config import get_settings
from packages.retrieval.vector_store import VectorStore


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()

    configure_logging()
    logger = get_logger("api")

    logger.info("application_startup", environment=settings.environment)

    vector_store = VectorStore()
    if not vector_store.health_check():
        logger.error("vector_store_connection_failed")
        raise RuntimeError("Qdrant is not reachable")

    logger.info("vector_store_connected")

    yield

    logger.info("application_shutdown")


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        lifespan=lifespan,
    )

    @app.get("/health")
    async def health_check():
        return {
            "status": "ok",
            "environment": settings.environment,
        }

    return app


app = create_app()