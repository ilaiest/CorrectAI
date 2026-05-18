import os
from dotenv import load_dotenv

load_dotenv()
ACTIVE_PROVIDER = os.getenv("ACTIVE_PROVIDER", "gemini")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite-preview")
HOTKEY = os.getenv("HOTKEY", "<ctrl>+<alt>+c")
EXIT_HOTKEY = os.getenv("EXIT_HOTKEY", "<ctrl>+<alt>+x")