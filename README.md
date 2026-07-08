# CorrectAI

CorrectAI is a local-first writing assistant for correcting spelling, accents, punctuation, and clearly misspelled words while preserving the user's tone and style.

The project currently supports terminal correction, clipboard correction, global hotkeys, automatic replacement of selected text, a minimal settings GUI, Gemini, and Ollama local models.

## Current Status

CorrectAI is still an early open source prototype, but the main correction workflows are functional.

Current features:

- Terminal correction mode.
- Clipboard correction mode.
- Global hotkey runner.
- Selection replacement workflow.
- Gemini provider.
- Ollama local provider.
- Minimal GUI for settings and starting the hotkey runner.
- `.env` configuration.
- Local-first architecture with no hosted backend.

Still in progress:

- More robust provider-specific error messages.
- Start/stop behavior for the GUI runner button.
- Provider connection testing.
- Quality and speed comparison between Gemini and local models.
- More complete setup documentation for different machines.

## Privacy Model

CorrectAI is designed to be local-first.

- API keys stay on the user's machine.
- Text is sent only to the selected provider.
- There is no hosted backend.
- There is no telemetry by default.
- Ollama can be used for local correction without sending text to a cloud provider.
- Users are responsible for reviewing each provider's privacy and data handling policies.

## Requirements

- Python 3.10 or newer.
- Git.
- Optional: a Gemini API key.
- Optional: Ollama for local models.

Install Python dependencies:

```powershell
py -m pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root. You can copy `.env.example` and adjust the values.

For Gemini:

```env
ACTIVE_PROVIDER=gemini
API_KEY=your_gemini_api_key_here
MODEL=gemini-3.1-flash-lite-preview
```

For Ollama:

```env
ACTIVE_PROVIDER=ollama
API_KEY=
MODEL=qwen2.5:7b
```

Recommended local models:

- `qwen2.5:7b` for better correction quality.
- `llama3.2:3b` for a lighter, faster option.
- `llama3.1:8b` as another higher-quality option if your machine can handle it.

## Ollama Setup

Install Ollama from:

```text
https://ollama.com/download
```

Download a model:

```powershell
ollama pull qwen2.5:7b
```

Check installed models:

```powershell
ollama list
```

Test the model:

```powershell
ollama run qwen2.5:7b
```

Remove an unused model:

```powershell
ollama rm llama3.2:3b
```

## Run Terminal Mode

```powershell
py main.py
```

Choose terminal mode and enter the text you want to correct.

## Run Clipboard Mode

```powershell
py main.py
```

Choose clipboard mode. CorrectAI reads the current clipboard text, corrects it, and copies the corrected text back to the clipboard.

## Run Hotkey Selection Mode

```powershell
py hotkey_runner.py
```

Then:

1. Select text in another application.
2. Press the configured hotkey.
3. CorrectAI simulates copy, corrects the selected text, and pastes the corrected text back into the active app.

For this workflow, a single-key hotkey such as `F8` is recommended. Hotkeys using `Ctrl`, `Alt`, `C`, or `V` can interfere with the simulated copy/paste flow.

Example configuration:

```env
HOTKEY=<f8>
EXIT_HOTKEY=<ctrl>+<alt>+x
```

Press the exit hotkey to stop the runner.

## Run GUI

```powershell
py gui.py
```

The GUI allows basic provider, API key, model, and hotkey configuration. It can also start the hotkey runner with the **Start CorrectAI** button.

Save settings before starting the runner so the active provider, model, and hotkey are loaded correctly.

## Project Direction

CorrectAI is planned as an open source desktop writing assistant with multiple correction workflows:

- Safe clipboard correction.
- Selection-based correction.
- Optional automatic replacement.
- Cloud providers such as Gemini.
- Local providers such as Ollama.
- A GUI for settings and manual correction.

The long-term goal is to make quick correction feel natural across apps like Slack, email, notes, browsers, and editors while keeping the code simple and auditable.
