from config import HOTKEY, EXIT_HOTKEY
from pynput import keyboard
from corrector import text_corrector
import pyperclip
import threading
import time 

is_correcting = False
keyboard_controller = keyboard.Controller()
hotkey_listener = None

def copy_selected_text():
    pyperclip.copy("")
    time.sleep(0.5)
    with keyboard_controller.pressed(keyboard.Key.ctrl):
        keyboard_controller.tap('c')
    time.sleep(0.5)
    copied_text = pyperclip.paste()
    clean_copied_text = copied_text.strip()
    return clean_copied_text

def correct_selected_text(selected_text):
    result = text_corrector(selected_text)
    return result['response']

def paste_corrected_text(corrected_text):
    pyperclip.copy(corrected_text)
    with keyboard_controller.pressed(keyboard.Key.ctrl):
        keyboard_controller.tap('v')
    print("Text corrected and pasted.")

def run_clipboard_correction():
    global is_correcting
    print("Hotkey activated! Running text correction...")
    try:
        time.sleep(0.2)
        selected_text = copy_selected_text()

        if not selected_text:
            print("No text selected")
            return
        corrected_text = correct_selected_text(selected_text)
        paste_corrected_text(corrected_text)

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
    stop_hotkey_listener()

def stop_hotkey_listener():
    global hotkey_listener
    if hotkey_listener is not None:
        hotkey_listener.stop()

def run_hotkey_listener(hotkey=HOTKEY, exit_hotkey=EXIT_HOTKEY):
    global hotkey_listener
    with keyboard.GlobalHotKeys({
        hotkey: on_activate,
        exit_hotkey: on_exit
    }) as listener:
        hotkey_listener = listener
        listener.join()
        hotkey_listener = None

if __name__ == "__main__":
    run_hotkey_listener()
