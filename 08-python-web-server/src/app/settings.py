# settings.py

import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    This class use pydantic_settings support to set Settings for the application.   
    """
    app_name: str = "Uvicorn_FastAPI"
    app_description: str = "Web server with FastAPI and Uvicorn"
    app_version: str = "0.0.1"
    admin_email: str = "giovanni.nocco@genocs.com"


    # Load the environment variables from the .env file
    # load_dotenv()

    # The following settings are loaded from the .env file
    azure_openai_model: str = ''
    openai_api_key: str = ''
    azure_openai_api_key: str = ''
    azure_openai_endpoint: str = ''

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    def set_env_vars(self):

        print("Setting environment variables")
        

        os.environ["AZURE_OPENAI_MODEL"] = self.azure_openai_model
        os.environ["OPENAI_API_KEY"] = self.openai_api_key
        os.environ["AZURE_OPENAI_API_KEY"] = self.azure_openai_api_key
        os.environ["AZURE_OPENAI_ENDPOINT"] = self.azure_openai_endpoint

        print("AZURE_OPENAI_MODEL: ", os.getenv("AZURE_OPENAI_MODEL"))


settings = Settings()
# settings.set_env_vars()