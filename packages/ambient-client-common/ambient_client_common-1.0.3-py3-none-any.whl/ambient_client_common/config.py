from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ambient_log_level: str = "INFO"
    backend_api_url: str = "https://api.ambientlabs.io"


settings = Settings()
