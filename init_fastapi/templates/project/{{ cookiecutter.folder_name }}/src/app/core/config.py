from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str
    BACKEND_CORS_ORIGINS: List[str]
    API_PREFIX: str

    description: str = """
        Description
    """

    debug: bool = True

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
