from config import HOTKEY, EXIT_HOTKEY
from pynput import keyboard
from corrector import text_corrector
import pyperclip
import threading

is_correcting = False


def run_clipboard_correction():
    global is_correcting
    print("Hotkey activated! Running text correction...")
    print("Reading from clipboard...")
    try:
        text = pyperclip.paste()
        clean_text = text.strip()
        if not clean_text:
            print("No text found in clipboard. Please copy some text and try again.")
            return
        result = text_corrector(clean_text)
        pyperclip.copy(result["response"])
        print("Text corrected and copied to clipboard.")
    finally:
        is_correcting = False


def on_activate():
    global is_correcting
    if is_correcting:
        print("Correction already running. Please wait.")
        return
    is_correcting = True
    threading.Thread(target=run_clipboard_correction, daemon=True).start()


def on_exit():
    print("Exit hotkey activated! Exiting the program...")
    listener.stop()

with keyboard.GlobalHotKeys({
    HOTKEY: on_activate,
    EXIT_HOTKEY: on_exit
}) as listener:
    listener.join()

