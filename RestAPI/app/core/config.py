from anyio.functools import lru_cache
from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

#  Settings for the database connection
class DatabaseSettings(BaseModel):
    database_name: SecretStr
    username: SecretStr
    password: SecretStr
    host: SecretStr
    port: int = 3600


class Settings(BaseSettings):

    db: DatabaseSettings

    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__"
    )

    @property
    def db_url(self) -> str:  # 화살표(->) 위치 수정
        return (
            f"mysql+aiomysql://{self.db.username.get_secret_value()}:"
            f"{self.db.password.get_secret_value()}@{self.db.host.get_secret_value()}:"
            f"{self.db.port}/{self.db.database_name.get_secret_value()}"
        )
# 캐싱되서 한번만 하면 ..연결시...
@lru_cache()
def get_settings() -> Settings:
    return Settings()
