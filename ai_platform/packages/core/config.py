from pydantic_settings import BaseSettings
from pydantic import Field
from pydantic import ConfigDict


class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=False,
    )

    # App
    app_name: str = Field(default="AI Production Intelligence Platform")
    environment: str = Field(default="development")
    log_level: str = Field(default="INFO")

    # Vector DB
    qdrant_url: str = Field(default="http://localhost:6333")

    # LLM
    default_model: str = Field(default="gpt-4o-mini")
    max_tokens: int = Field(default=2048)


def get_settings() -> Settings:
    return Settings()