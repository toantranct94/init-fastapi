from app.core.config import settings
from app.routers.health import router as health_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_application():
    _app = FastAPI(
        title=settings.APP_NAME,
        description=settings.description,
        debug=settings.debug,
        openapi_url=f"{settings.API_PREFIX}/api/openapi.json",
        docs_url=f'{settings.API_PREFIX}/docs',
        redoc_url=f'{settings.API_PREFIX}/redoc',
    )

    _app.include_router(health_router, prefix=settings.API_PREFIX)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
