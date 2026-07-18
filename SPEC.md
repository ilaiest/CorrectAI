# CorrectAI Spec

## Objective

CorrectAI is a local-first desktop tool for correcting selected text in place.

The v1 objective is simple:

```text
Select text in any app -> press a hotkey -> replace it with corrected text.
```

CorrectAI should fix spelling, accents, punctuation, and clearly misspelled words while preserving the user's tone, meaning, and style as much as possible.

## Product Scope

### In Scope For v1

- Correct selected text from other applications.
- Simulate copy from the active selection.
- Read selected text from the clipboard.
- Correct text with the active provider.
- Copy corrected text back to the clipboard.
- Paste corrected text into the active application.
- Provide a GUI for provider, model, API key, and hotkey configuration.
- Support Gemini.
- Support Ollama local models.
- Keep configuration local through `.env`.

### Out Of Scope For v1

- Chatbot mode.
- Email drafting.
- Long-form writing assistant.
- Tone rewriting modes.
- Multi-step agent workflows.
- Hosted backend.
- Telemetry.

## Product Principles

- Correct only what is necessary.
- Preserve the user's tone and intent.
- Avoid making text more formal unless explicitly requested.
- Return only the corrected text for the replacement workflow.
- Keep user credentials local.
- Make provider and model configuration explicit.
- Prefer local/offline options when practical.
- Keep the code simple, readable, and auditable.

## Open Source Principles

CorrectAI should be understandable and safe for other users to run on their own machines.

- No hosted backend by default.
- No telemetry by default.
- No API keys committed to the repository.
- No hidden provider calls.
- Text should only be sent to the selected provider.
- Local providers should be supported for users who prefer privacy or lower-cost usage.
- Forks, issues, and pull requests should be welcome.
- The code should stay approachable for people who are learning.

## Current Architecture

```text
gui.py
  settings UI
  hotkey normalization/display
  starts and stops the hotkey runner process

hotkey_runner.py
  listens for global hotkeys
  copies selected text
  calls the correction core
  pastes corrected text back into the active app

main.py
  terminal and clipboard test modes

corrector.py
  builds the correction prompt
  selects the active provider
  returns normalized correction output

providers/
  base.py
    shared provider interface

  gemini_provider.py
    Gemini implementation

  ollama_provider.py
    Ollama implementation

config.py
  loads `.env` configuration
```

## Correction Flow

```text
selected text
  -> simulated Ctrl+C
  -> clipboard
  -> corrector.py
  -> active provider
  -> corrected text
  -> clipboard
  -> simulated Ctrl+V
```

## Providers

### Gemini

Cloud provider option for users with a Gemini API key.

### Ollama

Local provider option for users who want lower-cost or private local correction.

Recommended local model for v1:

```text
qwen2.5:7b
```

This model has been a good balance between correction quality and reasonable local resource usage.

## Hotkey Behavior

The recommended default hotkey is:

```text
F8
```

The internal `pynput` format is:

```text
<f8>
```

The GUI should display user-friendly hotkeys such as:

```text
F8
Ctrl+Alt+Q
```

and save them internally as:

```text
<f8>
<ctrl>+<alt>+q
```

Hotkeys involving `Ctrl`, `Alt`, `C`, or `V` may interfere with simulated copy/paste and should not be the recommended default.

## GUI Requirements

The v1 GUI should remain a small configuration and control surface.

Required:

- Select provider.
- Set API key.
- Set model.
- Set hotkey.
- Save settings.
- Start CorrectAI.
- Stop CorrectAI.
- Show basic status messages.

Not required for v1:

- Chat interface.
- Text editor.
- Message composer.
- Provider connection tester.

## Safety Notes

CorrectAI uses clipboard and keyboard automation. This means behavior may vary by application.

The v1 workflow should be tested in common writing surfaces:

- Notepad.
- VSCode.
- Browser text fields.
- Email clients.
- Slack or similar messaging apps.

If a target app does not allow standard copy/paste shortcuts, the replacement workflow may not work reliably.

## Future Directions

Future versions may explore:

- Compose mode for messages and emails.
- Tone adjustment.
- Optional explanation of corrections.
- Provider connection testing.
- Packaged desktop release.
- Tray/background app behavior.
