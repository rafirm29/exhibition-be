from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_ADMIN: str
    MONGODB_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()