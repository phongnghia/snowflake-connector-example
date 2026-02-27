# settings.py
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def get_env(name: str, required: bool = True, default=None):
    value = os.getenv(name, default)
    if required and not value:
        print(f"Missing required environment variable: {name}")
        sys.exit(1)
    return value


class Settings:
  # Load environment variables
  ACCOUNT_INDENTIFIER = get_env("ACCOUNT_INDENTIFIER", required=True)
  USER = get_env("USER", required=True)
  PASSWORD = get_env("PASSWORD", required=True)
  ROLE = get_env("ROLE", required=True)
  WAREHOUSE = get_env("WAREHOUSE", required=True)
  DATABASE = get_env("DATABASE", required=True)
  SCHEMA = get_env("SCHEMA", required=True)
