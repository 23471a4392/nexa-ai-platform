"""Centralized application and environment configuration for NexaAI."""
import os
from dataclasses import dataclass

@dataclass
class Config:
    ENV: str = os.getenv("NEXA_ENV", "development")
    DEBUG: bool = os.getenv("NEXA_DEBUG", "True").lower() in ("true", "1", "yes")
    HOST: str = os.getenv("NEXA_HOST", "0.0.0.0")
    PORT: int = int(os.getenv("NEXA_PORT", "8000"))
    SECRET_KEY: str = os.getenv("NEXA_SECRET_KEY", "nexa-default-dev-secret-key-3.7")
    API_PREFIX: str = "/api"
    DEFAULT_MODEL: str = os.getenv("NEXA_DEFAULT_MODEL", "Nexa Reasoner")
    MAX_TOKENS_PER_REQUEST: int = int(os.getenv("NEXA_MAX_TOKENS", "4096"))
    RATE_LIMIT_PER_MINUTE: int = int(os.getenv("NEXA_RATE_LIMIT", "120"))
    ENABLE_METRICS: bool = os.getenv("NEXA_ENABLE_METRICS", "True").lower() in ("true", "1", "yes")

config = Config()
