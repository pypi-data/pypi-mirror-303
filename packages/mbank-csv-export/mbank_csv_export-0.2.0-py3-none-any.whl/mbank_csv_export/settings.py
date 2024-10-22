from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mbank_username: Optional[str] = None
    mbank_password: Optional[str] = None
    mbank_log_level: str = "INFO"
