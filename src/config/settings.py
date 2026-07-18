from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "StadiumMind AI"
    environment: str = "development"
    debug: bool = True
    llm_api_key: str = "mock_key_for_now"
    
    # Security Policies
    allowed_origins: List[str] = ["http://localhost:5173", "https://stadiummind-ai.vercel.app"]
    rate_limit: str = "5/minute"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
