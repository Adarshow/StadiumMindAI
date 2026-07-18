from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "StadiumMind AI"
    environment: str = "development"
    debug: bool = True
    llm_api_key: str = "mock_key_for_now"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
