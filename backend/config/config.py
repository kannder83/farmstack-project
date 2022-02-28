from pydantic import BaseSettings


class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_hostname: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    production_environment: bool

    class Config:
        env_file = ".env"


settings = Settings()
