# CorrectAI

CorrectAI is a local-first desktop tool that corrects selected text in place.

Select text in any app, press your hotkey, and CorrectAI replaces it with a corrected version while preserving your tone as much as possible.

<p align="center">
<img width="416" height="540" alt="image" src="https://github.com/user-attachments/assets/83da2135-7f07-447a-85f0-ca8cc2e64281" />
</p>

## Why This Exists

CorrectAI is part of a personal series of weekend projects.

The goal is to keep practicing programming, avoid getting rusty, and keep learning by building small tools that solve real problems. I use AI as a learning partner during the process, but the point is not to let AI build everything for me. The point is to understand the code, make decisions, debug issues, and keep improving my own engineering skills.

This first project started from a simple annoyance: writing emails, Slack messages, notes, or quick replies on a computer and not having a fast, system-wide way to correct spelling without copying text into another app.

So CorrectAI became a way to explore a practical question:

```text
Can I build a low-cost or local AI correction tool that works directly where I am writing?
```

## Open Source

CorrectAI is open source. If this project is useful, interesting, or close to something you want to improve, feel free to fork it, open an issue, suggest changes, or build your own version.

This project is also meant to be readable for people who are learning. The code favors simple structure over clever abstractions so it is easier to inspect, modify, and learn from.

## What It Does

Current v1 focus:

- Correct selected text directly in the active app.
- Preserve tone and meaning.
- Avoid rewriting more than necessary.
- Support Gemini as a cloud provider.
- Support Ollama as a local provider.
- Provide a small GUI for settings and starting/stopping the runner.

Out of scope for v1:

- Chatbot writing assistant.
- Email drafting.
- Tone rewriting modes.
- Long-form composition.

Those may come later, but v1 is intentionally focused on fast in-place correction.

## Current Features

- Terminal correction mode.
- Clipboard correction mode.
- Global hotkey runner.
- Selection replacement workflow.
- Gemini provider.
- Ollama provider.
- GUI for provider, model, API key, and hotkey settings.
- Local-first architecture with no hosted backend.

## Privacy Model

- API keys stay on your machine.
- Text is sent only to the selected provider.
- There is no hosted backend.
- There is no telemetry by default.
- Ollama can be used for local correction without sending text to a cloud provider.

Users are responsible for reviewing each provider's privacy and data handling policies.

## Requirements

- Python 3.10 or newer.
- Git.
- Optional: a Gemini API key.
- Optional: Ollama for local correction.

Install dependencies:

```powershell
py -m pip install -r requirements.txt
```

## Windows Release

For non-technical users, the recommended way to try CorrectAI is to download the Windows executable from GitHub Releases.

Download:

```text
CorrectAI.exe
```

Then open the app, choose a provider, save your settings, and press **Start CorrectAI**.

The Windows executable does not include Ollama or local models. If you want to use local correction, install Ollama and download the recommended model first. See [OLLAMA_SETUP.md](OLLAMA_SETUP.md).

## Configuration

Create a `.env` file in the project root. You can copy `.env.example` and adjust the values.

Recommended local setup:

```env
ACTIVE_PROVIDER=ollama
API_KEY=
MODEL=qwen2.5:7b
HOTKEY=<f8>
EXIT_HOTKEY=<ctrl>+<alt>+x
```

Gemini setup:

```env
ACTIVE_PROVIDER=gemini
API_KEY=your_gemini_api_key_here
MODEL=gemini-3.1-flash-lite-preview
HOTKEY=<f8>
EXIT_HOTKEY=<ctrl>+<alt>+x
```

## Ollama Setup

Install Ollama:

```text
https://ollama.com/download
```

For a step-by-step setup guide, see [OLLAMA_SETUP.md](OLLAMA_SETUP.md).

Recommended local model:

```powershell
ollama pull qwen2.5:7b
```

Useful commands:

```powershell
ollama list
ollama run qwen2.5:7b
ollama rm llama3.2:3b
```

`qwen2.5:7b` has worked well as a local balance between correction quality and reasonable resource usage.

## Run The GUI

```powershell
py gui.py
```

From the GUI you can:

- Select provider.
- Set API key.
- Set model.
- Set hotkey.
- Save settings.
- Start or stop CorrectAI.

Recommended hotkey:

```text
F8
```

Hotkeys using `Ctrl`, `Alt`, `C`, or `V` can interfere with the simulated copy/paste workflow.

## Run Hotkey Mode Directly

```powershell
py hotkey_runner.py
```

Then:

1. Select text in any app.
2. Press the configured hotkey.
3. CorrectAI simulates copy.
4. CorrectAI sends the text to the active provider.
5. CorrectAI pastes the corrected text back into the active app.

If you run the hotkey runner directly, use the exit hotkey to stop it:

```text
Ctrl+Alt+X
```

## Run Terminal Or Clipboard Mode

```powershell
py main.py
```

The terminal menu includes:

- Terminal input correction.
- Clipboard correction.

These modes are useful for testing, but the main v1 workflow is the GUI + hotkey replacement flow.

## Project Direction

CorrectAI v1 is intentionally small:

```text
Selected text -> hotkey -> correction -> replacement
```

Future versions may explore a compose mode, message drafting, tone adjustment, or a chatbot-style assistant. For now, the priority is keeping the core workflow simple, understandable, and useful.

## Credits

- Verificado iconos creados por NX Icon - Flaticon: https://www.flaticon.es/iconos-gratis/verificado

## License

MIT License. See [LICENSE](LICENSE).
