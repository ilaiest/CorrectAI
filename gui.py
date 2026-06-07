import customtkinter as ctk
import os
from dotenv import load_dotenv

load_dotenv()

ACTIVE_PROVIDER = os.getenv("ACTIVE_PROVIDER", "gemini")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL", "gemini-3.1-flash-lite-preview")
HOTKEY = os.getenv("HOTKEY", "<ctrl>+<alt>+c")
EXIT_HOTKEY = os.getenv("EXIT_HOTKEY", "<ctrl>+<alt>+x")


def test_con_logic():
    pass


def save_logic():
    with open(".env", "w") as f:
        f.write(f"ACTIVE_PROVIDER={provider_dropdown.get()}\n")
        f.write(f"HOTKEY={hotkey_entry.get()}\n")
        f.write(f"API_KEY={api_key_entry.get()}\n")
        f.write(f"MODEL={model_entry.get()}\n")
    changes_saved_label.configure(text="Saved! ✅", text_color="green")


app = ctk.CTk()
app.title("CorrectAI Settings")
app.geometry("300x400")
#Providers
provider_label = ctk.CTkLabel(app, text="Provider")
provider_label.pack()
provider_dropdown = ctk.CTkOptionMenu(app, values=["gemini", "ollama", "claude - Amazon Bedrock"])
provider_dropdown.pack()
provider_dropdown.set(ACTIVE_PROVIDER)
#API KEY
api_key_label = ctk.CTkLabel(app, text="API Key")
api_key_label.pack(pady=5)
api_key_entry = ctk.CTkEntry(app, show="*", placeholder_text="Enter Your API KEY here")
api_key_entry.pack()
api_key_entry.insert(0,API_KEY or "")
#Model
model_label = ctk.CTkLabel(app, text="Model")
model_label.pack(pady=5)
model_entry = ctk.CTkEntry(app, placeholder_text="Enter the model name")
model_entry.pack()
model_entry.insert(0,MODEL or "")
#Hotkey combination
hotkey_label = ctk.CTkLabel(app, text="Hot Key Combination")
hotkey_label.pack(pady=5)
hotkey_entry = ctk.CTkEntry(app, placeholder_text="Enter your hotkey combination")
hotkey_entry.pack()
hotkey_entry.insert(0,HOTKEY or "")
#Test Connection Button
test_con_button = ctk.CTkButton(app, text="Test Connection(Coming Soon)")
test_con_button.pack(pady=(30,15))
#Save Button
save_button = ctk.CTkButton(app, text="Save", command=save_logic)
save_button.pack(pady=15)
changes_saved_label = ctk.CTkLabel(app, text="")
changes_saved_label.pack()
app.mainloop()