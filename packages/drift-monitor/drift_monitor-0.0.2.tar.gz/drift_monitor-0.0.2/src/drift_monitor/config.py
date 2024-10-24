"""Configuration module for drift_monitor detection client."""

import datetime as dt

import jwt
from libmytoken import MytokenServer
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings class for drift_monitor detection client."""

    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    DRIFT_MONITOR_URL: str
    DRIFT_MONITOR_API_VERSION: str = "v1"
    DRIFT_MONITOR_TIMEOUT: int = 10

    DRIFT_MONITOR_MYTOKEN: str
    MYTOKEN_SERVER: str = "https://mytoken.data.kit.edu/"
    # MYTOKEN_SERVER: str = "https://mytok.eu"

    TESTING: bool = False

    @property
    def monitor_url(self) -> str:
        """Get the monitor URL."""
        return f"{self.DRIFT_MONITOR_URL}/api/{self.DRIFT_MONITOR_API_VERSION}"


class AccessToken:
    """Access token class for mytoken server."""

    def __init__(self):
        self._at = MytokenServer(settings.MYTOKEN_SERVER).AccessToken
        self.value = None
        self.decode_options = {
            "algorithms": ["HS256"],
            "options": {"verify_signature": False},
        }
        self.info = {"exp": 0}

    def __call__(self):
        """Get the access token from mytoken server."""
        if self.info["exp"] < dt.datetime.now(dt.timezone.utc).timestamp():
            self.value = self._at.get(settings.DRIFT_MONITOR_MYTOKEN)
            self.info = jwt.decode(self.value, **self.decode_options)
        return self.value


# Initialize the settings object
settings = Settings()
access_token = AccessToken()
