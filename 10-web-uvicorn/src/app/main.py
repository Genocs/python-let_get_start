# memory.py

import os
import logging
from functools import lru_cache
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.settings import Settings

from app.routes.main import router as main_router

# Set up logging
logging.basicConfig(level=logging.DEBUG,
                    style='{', format='{levelname}: {asctime} -{name}: {message}')
log = logging.getLogger("gnx-app")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
settings.set_env_vars()

app = FastAPI(title=settings.app_name,
              description=settings.app_description,
              version=settings.app_version)

# CORS
origins = ["*"]

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(main_router, prefix="/api/v1/main", tags=["main"])


@app.get("/health")
async def ping():
    """
    Health check endpoint    
    """
    log.info(os.getenv("AZURE_OPENAI_MODEL"))
    log.debug("Health check")
    return {"status": "Ok"}


@app.get("/info")
async def info(info_settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": info_settings.app_name,
        "app_description": info_settings.app_description,
        "app_version": info_settings.app_version,
        "admin_email": info_settings.admin_email,
        "azure_openai_model": info_settings.azure_openai_model
    }


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/redoc')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
