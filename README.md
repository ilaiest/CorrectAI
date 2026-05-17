# CorrectAI

CorrectAI is a local-first writing assistant for correcting spelling, accents, and punctuation with AI while preserving the user's tone and wording as much as possible.

The current version is a small terminal prototype that sends text to Gemini, returns a corrected version, lists a few important changes, and shows the execution time.

## Current Status

CorrectAI is in an early prototype stage.

Current features:

- Terminal input.
- Empty text validation.
- Gemini API integration.
- Short correction prompt.
- Basic API error handling.
- Execution time measurement.

Not available yet:

- Clipboard support.
- Global hotkeys.
- Graphical interface.
- Multiple AI providers.
- Local model support.
- Persistent settings.

## Privacy Model

CorrectAI is designed to be local-first.

- API keys should stay on the user's machine.
- Text is sent only to the provider selected by the user.
- There is no hosted backend.
- There is no telemetry by default.
- Users are responsible for reviewing their provider's privacy and data handling policies.

## Requirements

- Python 3.10 or newer.
- A Gemini API key.
- The `google-genai` package.

Install the Gemini SDK:

```powershell
py -m pip install -U google-genai
```

## Configure Gemini

Set your Gemini API key in the current PowerShell session:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

Verify that Python can read it:

```powershell
py -c "import os; print(os.getenv('GEMINI_API_KEY'))"
```

This environment variable is temporary. If you close the terminal, you need to set it again.

## Run

```powershell
py main.py
```

Then enter the text you want to correct.

## Project Direction

CorrectAI is planned as an open source tool that can support multiple AI providers:

- Gemini for accessible cloud-based usage.
- AWS Bedrock for users with enterprise or cloud credentials.
- Ollama or another local provider for private/offline usage.
- A mock provider for development and testing.

The long-term goal is to support clipboard correction and optional global hotkeys so users can correct selected text from other applications.

