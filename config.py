import os
from dotenv import load_dotenv

load_dotenv()
ACTIVE_PROVIDER = os.getenv("ACTIVE_PROVIDER", "gemini")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL", "gemini-3.1-flash-lite-preview")
HOTKEY = os.getenv("HOTKEY", "<f8>")
EXIT_HOTKEY = os.getenv("EXIT_HOTKEY", "<ctrl>+<alt>+x")
