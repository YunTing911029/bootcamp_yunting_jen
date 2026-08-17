from pathlib import Path
from dotenv import load_dotenv
import sys, os
load_dotenv()  # looks for a .env file in the current and parent directories
print(".env loaded (if present)")

# src/config.py (inline demo)
from typing import Optional

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"
print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)