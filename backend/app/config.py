from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    MONGO_DB_NAME: str = "ai_lms"
    JWT_SECRET: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
