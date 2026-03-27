from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    # ==================== SERVER CONFIGURATION ====================
    HOST: str = Field(default="0.0.0.0", description="Server host")
    PORT: int = Field(default=8000, description="Server port")
    ENVIRONMENT: str = Field(default="development", description="Environment")
    APP_NAME: str = Field(default="Data Science POC", description="Application name")
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")

    # ==================== JWT CONFIGURATION ====================
    JWT_SECRET_KEY: str = Field(default="change-me-in-production", description="JWT secret key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=1440, description="Token expiry in minutes")

    # ==================== EXTERNAL SERVICES ====================
    FRONTEND_URL: str = Field(default="http://localhost:3000", description="Frontend URL")

    # Helper properties
    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT.lower() == "production"

    @property
    def is_development(self) -> bool:
        return self.ENVIRONMENT.lower() == "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
