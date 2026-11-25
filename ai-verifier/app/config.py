"""Configurazione del servizio di verifica.

Tutti i parametri (versione della pipeline, e in seguito soglie, chiavi e indirizzi)
si leggono dalle variabili d'ambiente o dal file `.env`, mai dal codice (RNF-MAN-03).
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Impostazioni del servizio lette dall'ambiente o dal file `.env`."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    pipeline_version: str = "0.1.0"


@lru_cache
def get_settings() -> Settings:
    """Restituisce le impostazioni, lette una sola volta all'avvio."""
    return Settings()
