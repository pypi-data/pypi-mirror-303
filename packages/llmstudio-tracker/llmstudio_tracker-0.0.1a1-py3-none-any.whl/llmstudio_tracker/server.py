from threading import Event

import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from llmstudio_tracker.config import TRACKING_HOST, TRACKING_PORT
from llmstudio_tracker.logs.endpoints import LogsRoutes
from llmstudio_tracker.session.endpoints import SessionsRoutes

TRACKING_HEALTH_ENDPOINT = "/health"
TRACKING_TITLE = "LLMstudio Tracking API"
TRACKING_DESCRIPTION = "The tracking API for LLM interactions"
TRACKING_VERSION = "0.0.1"
TRACKING_BASE_ENDPOINT = "/api/tracking"


## Tracking
def create_tracking_app(started_event: Event) -> FastAPI:
    app = FastAPI(
        title=TRACKING_TITLE,
        description=TRACKING_DESCRIPTION,
        version=TRACKING_VERSION,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get(TRACKING_HEALTH_ENDPOINT)
    def health_check():
        """Health check endpoint to ensure the API is running."""
        return {"status": "healthy", "message": "Tracking is up and running"}

    tracking_router = APIRouter(prefix=TRACKING_BASE_ENDPOINT)
    LogsRoutes(tracking_router)
    SessionsRoutes(tracking_router)

    app.include_router(tracking_router)

    @app.on_event("startup")
    async def startup_event():
        started_event.set()
        print(f"Running LLMstudio Tracking on http://{TRACKING_HOST}:{TRACKING_PORT} ")

    return app


def run_tracker_app(started_event: Event):
    try:
        tracking = create_tracking_app(started_event)
        uvicorn.run(
            tracking,
            host=TRACKING_HOST,
            port=TRACKING_PORT,
            log_level="warning",
        )
    except Exception as e:
        print(f"Error running LLMstudio Tracking: {e}")
