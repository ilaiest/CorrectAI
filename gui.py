import customtkinter as ctk
import os
from dotenv import load_dotenv
import subprocess
import sys
from pathlib import Path

ctk.set_appearance_mode("dark")
runner_process = None

BG_COLOR = "#24292E"
PRIMARY_COLOR = "#415156"
PRIMARY_HOVER = "#52666C"
SECONDARY_COLOR = "#30383D"
SECONDARY_HOVER = "#3A464C"
INPUT_COLOR = "#2B3237"
BORDER_COLOR = "#415156"
TEXT_COLOR = "#EDF0F2"
MUTED_TEXT_COLOR = "#AEB7BE"
SUCCESS_COLOR = "#808A92"

LABEL_FONT = ("Segoe UI Variable", 14)
INPUT_FONT = ("Segoe UI Variable", 13)
BUTTON_FONT = ("Segoe UI Variable", 14, "bold")

load_dotenv()

ACTIVE_PROVIDER = os.getenv("ACTIVE_PROVIDER", "gemini")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL", "gemini-3.1-flash-lite-preview")
HOTKEY = os.getenv("HOTKEY", "<f8>")
EXIT_HOTKEY = os.getenv("EXIT_HOTKEY", "<ctrl>+<alt>+x")

def start_runner():
    global runner_process

    if runner_process is not None and runner_process.poll() is None:
        #already running
        return
    runner_path = Path(__file__).with_name("hotkey_runner.py")
    runner_process = subprocess.Popen([sys.executable, str(runner_path)])
    changes_saved_label.configure(text="CorrectAI is running! ✅", text_color=SUCCESS_COLOR)

def test_con_logic():
    pass

def normalize_hotkey(user_input):
    special_keys = {
        "ctrl": "<ctrl>",
        "control": "<ctrl>",
        "alt": "<alt>",
        "shift": "<shift>",
        "space": "<space>",
        "enter": "<enter>",
        "esc": "<esc>",
        "escape": "<esc>",
        "tab": "<tab>",
    }

    cleaned_input = user_input.strip().lower().replace(" ", "")
    parts = cleaned_input.split("+")

    normalized_parts = []

    for part in parts:
        if part in special_keys:
            normalized_parts.append(special_keys[part])
        elif part.startswith("f") and part[1:].isdigit():
            normalized_parts.append(f"<{part}>")
        else:
            normalized_parts.append(part)

    return "+".join(normalized_parts)

def save_logic():
    with open(".env", "w") as f:
        f.write(f"ACTIVE_PROVIDER={provider_dropdown.get()}\n")
        hotkey_value = normalize_hotkey(hotkey_entry.get())
        f.write(f"HOTKEY={hotkey_value}\n")
        f.write(f"API_KEY={api_key_entry.get()}\n")
        f.write(f"MODEL={model_entry.get()}\n")
        f.write(f"EXIT_HOTKEY={EXIT_HOTKEY}\n")
    changes_saved_label.configure(text="Saved! ✅", text_color=SUCCESS_COLOR)

app = ctk.CTk()
app.title("CorrectAI Settings")
app.geometry("420x520")
app.configure(fg_color=BG_COLOR)
content_frame = ctk.CTkFrame(app, fg_color="transparent")
content_frame.pack(pady=(42, 0))
#Providers
provider_label = ctk.CTkLabel(content_frame, text="Provider", text_color=TEXT_COLOR, font=LABEL_FONT)
provider_label.pack()
provider_dropdown = ctk.CTkOptionMenu(
    content_frame,
    values=["gemini", "ollama"],
    fg_color=INPUT_COLOR,
    button_color=PRIMARY_COLOR,
    button_hover_color=PRIMARY_HOVER,
    text_color=TEXT_COLOR,
    dropdown_fg_color=INPUT_COLOR,
    dropdown_hover_color=SECONDARY_COLOR,
    dropdown_text_color=TEXT_COLOR,
    font=INPUT_FONT,
    dropdown_font=INPUT_FONT,
)
provider_dropdown.pack()
provider_dropdown.set(ACTIVE_PROVIDER)
#API KEY
api_key_label = ctk.CTkLabel(content_frame, text="API Key", text_color=TEXT_COLOR, font=LABEL_FONT)
api_key_label.pack(pady=5)
api_key_entry = ctk.CTkEntry(
    content_frame,
    show="*",
    placeholder_text="Enter Your API KEY here",
    fg_color=INPUT_COLOR,
    border_color=BORDER_COLOR,
    text_color=TEXT_COLOR,
    placeholder_text_color=MUTED_TEXT_COLOR,
    font=INPUT_FONT,
)
api_key_entry.pack()
api_key_entry.insert(0,API_KEY or "")
#Model
model_label = ctk.CTkLabel(content_frame, text="Model", text_color=TEXT_COLOR, font=LABEL_FONT)
model_label.pack(pady=5)
model_entry = ctk.CTkEntry(
    content_frame,
    placeholder_text="Enter the model name",
    fg_color=INPUT_COLOR,
    border_color=BORDER_COLOR,
    text_color=TEXT_COLOR,
    placeholder_text_color=MUTED_TEXT_COLOR,
    font=INPUT_FONT,
)
model_entry.pack()
model_entry.insert(0,MODEL or "")
#Hotkey combination
hotkey_label = ctk.CTkLabel(content_frame, text="Hot Key Combination", text_color=TEXT_COLOR, font=LABEL_FONT)
hotkey_label.pack(pady=5)
hotkey_entry = ctk.CTkEntry(
    content_frame,
    placeholder_text="Enter your hotkey combination",
    fg_color=INPUT_COLOR,
    border_color=BORDER_COLOR,
    text_color=TEXT_COLOR,
    placeholder_text_color=MUTED_TEXT_COLOR,
    font=INPUT_FONT,
)
hotkey_entry.pack()
hotkey_entry.insert(0,HOTKEY or "")
#Save Button
save_button = ctk.CTkButton(content_frame, text="Save", command=save_logic, width=220, height=36, fg_color=SECONDARY_COLOR, hover_color=SECONDARY_HOVER, text_color=TEXT_COLOR, corner_radius=8, font=BUTTON_FONT)
save_button.pack(pady=(50,12))
changes_saved_label = ctk.CTkLabel(content_frame, text="", text_color=MUTED_TEXT_COLOR, font=LABEL_FONT)
changes_saved_label.pack()
#Run Button
run_button = ctk.CTkButton(content_frame, text="Start CorrectAI" , command=start_runner, width=220, height=44, fg_color=PRIMARY_COLOR, hover_color=PRIMARY_HOVER, text_color="#FFFFFF", corner_radius=8, font=BUTTON_FONT)
run_button.pack(pady=15)
app.mainloop()
