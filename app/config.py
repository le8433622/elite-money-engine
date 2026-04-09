import os


class Settings:
    app_name: str = os.getenv("APP_NAME", "Elite Money Engine")
    secret_key: str = os.getenv("SECRET_KEY", "change-me")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./elite_money_engine.db")


settings = Settings()
