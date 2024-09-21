# settings.py

import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings for the application.
    """
    app_name: str = "Uvicorn_FastAPI"
    app_description: str = "Web server with FastAPI and Uvicorn"
    app_version: str = "0.0.1"
    admin_email: str = "giovanni.nocco@genocs.com"

##    model_config = SettingsConfigDict(env_file="../.env")
    os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
#    os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")
#    os.environ["AZURE_OPENAI_MODEL"] = os.getenv("AZURE_OPENAI_MODEL")
    AZURE_OPENAI_MODEL: str

    # os.environ["AZURE_COGNITIVE_SEARCH_SERVICE_NAME"] = os.getenv("AZURE_COGNITIVE_SEARCH_SERVICE_NAME")
    # os.environ["AZURE_COGNITIVE_SEARCH_INDEX_NAME"] = os.getenv("AZURE_COGNITIVE_SEARCH_INDEX_NAME")
    # os.environ["AZURE_COGNITIVE_SEARCH_API_KEY"] = os.getenv("AZURE_COGNITIVE_SEARCH_API_KEY")

settings = Settings()
