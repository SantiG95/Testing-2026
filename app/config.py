from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str = "ecommerce"
    DB_USERNAME: str
    DB_PASSWORD: str

    JWT_SECRET: str = "MiSuperSecretoJwtClave123456789012"
    JWT_EXPIRATION: int = 86400000  # milisegundos

    PORT: int = 8080

    class Config:
        env_file = ".env"

    @property
    def database_url(self) -> str:
        return f"mysql+pymysql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
